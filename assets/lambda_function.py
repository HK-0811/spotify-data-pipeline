import boto3
import json
import time

glue = boto3.client('glue')
s3 = boto3.client('s3')

# Glue job and crawler names
GLUE_JOB_NAME = "spotify-pipeline"
CRAWLER_NAME = "spotify-data-crawler"

def lambda_handler(event, context):
    # Log S3 event details
    print("Received event: ", json.dumps(event, indent=2))

    # Extract bucket and key from S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Remove old data from S3
    try:
        # List objects in the specified folder
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=key)
        
        # Check if the folder contains any files
        if 'Contents' in response:
            files_to_delete = [
                {'Key': obj['Key']} for obj in response['Contents'] if obj['Key'].endswith('.parquet')
            ]
            
            if files_to_delete:
                # Delete the files in batches (max 1000 per request)
                delete_response = s3.delete_objects(
                    Bucket=bucket_name,
                    Delete={'Objects': files_to_delete}
                )
                print(f"Deleted files: {delete_response.get('Deleted', [])}")
            else:
                print("No Parquet files found to delete.")
        else:
            print("The folder is empty or does not exist.")

    except Exception as e:
        print(f"An error occurred: {e}")

    
    # Trigger Glue job
    try:
        response = glue.start_job_run(JobName=GLUE_JOB_NAME)
        job_run_id = response['JobRunId']
        print(f"Started Glue Job {GLUE_JOB_NAME}, JobRunID: {job_run_id}")
    except Exception as e:
        print(f"Failed to start Glue job: {e}")
        return {'statusCode': 500, 'body': f"Glue job failed: {e}"}

    # Wait for Glue job to finish
    job_status = wait_for_job_completion(GLUE_JOB_NAME, job_run_id)
    if job_status != 'SUCCEEDED':
        print(f"Glue Job {GLUE_JOB_NAME} failed with status: {job_status}")
        return {'statusCode': 500, 'body': f"Glue job failed with status: {job_status}"}

    

    # Trigger Glue crawler
    try:
        glue.start_crawler(Name=CRAWLER_NAME)
        print(f"Started Glue Crawler {CRAWLER_NAME}")
    except Exception as e:
        print(f"Failed to start Glue crawler: {e}")
        return {'statusCode': 500, 'body': f"Crawler failed: {e}"}
    
    return {'statusCode': 200, 'body': "Automation pipeline executed successfully"}

def wait_for_job_completion(job_name, job_run_id):
    while True:
        response = glue.get_job_run(JobName=job_name, RunId=job_run_id)
        status = response['JobRun']['JobRunState']
        if status in ['SUCCEEDED', 'FAILED', 'STOPPED']:
            return status
        time.sleep(15)  # Poll every 15 seconds
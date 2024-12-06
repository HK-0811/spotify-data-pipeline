from s3fs import S3FileSystem


# connect to s3
def connect_to_s3(client_id,secret_key):
    try:
        s3 = S3FileSystem(anon=False,key=client_id,secret=secret_key)
        print("Connection to S3 Successfull")
        return s3
    except Exception as e:
        print(e)

# create bucket
def create_bucket_if_not_exists(s3:S3FileSystem,bucket:str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print(f"Bucket {bucket} created")
        else:
            print(f"Bucket {bucket} already exists")
    except Exception as e:
        print(e)



# upload to s3
def upload_to_s3(s3:S3FileSystem,file_path:str,bucket:str,s3_file_name:str):
    try:
        s3.put(file_path, bucket + '/raw2/' + s3_file_name)
        print(f'{s3_file_name} uploaded to {bucket}')
    except FileNotFoundError:
        print(f"File {file_path} not found")

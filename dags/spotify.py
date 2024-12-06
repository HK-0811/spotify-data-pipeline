from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import os
import sys

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.spotify_pipeline import spotify_pipeline
from pipelines.aws_pipeline import upload_s3_pipeline


default_args = {
    "owner" : "Himanshu Kotkar",
    "start_date" : datetime(2024,11,22)
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id = 'spotify_pipeline',
    default_args = default_args,
    schedule_interval='@weekly',
    catchup= False
)


# connect and extract data to s3
extract = PythonOperator(
    task_id='spotify_data_extraction',
    python_callable=spotify_pipeline,
    op_kwargs= {
        'file_name':f'spotify_{file_postfix}',
        'playlist_link':'https://open.spotify.com/playlist/3vaFOIAhoVXb1nnw0uhylC'
    },
    dag=dag
)


# loading to s3
upload_s3 = PythonOperator(
    task_id='upload_s3',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3
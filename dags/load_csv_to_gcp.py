import os
from datetime import timedelta
from datetime import datetime

from airflow import DAG
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.contrib.operators.gcs_delete_operator import GoogleCloudStorageDeleteOperator

BASE_DIR = "/home/maksym/Data-Engineering-Golovata/lesson02/ht_template/data/stg/sales"
STG_DIR = os.path.join(BASE_DIR, "{{ ds }}")
BUCKET_NAME = 'de-07-m-o'
PATH = 'src1/sales/v1'

dag = DAG(
    dag_id='load_to_gcp',
    start_date=datetime(2022, 8, 9),
    end_date=datetime(2022, 8, 11),
    schedule_interval="0 1 * * *",
    catchup=True,
    max_active_runs=1,
)

upload_sales = LocalFilesystemToGCSOperator(
    task_id="upload_sales",
    src = STG_DIR + '/*.avro',
    dst= os.path.join(
        PATH,
        'year={{ execution_date.strftime("%Y") }}',
        'month={{ execution_date.strftime("%m") }}',
        'day={{ execution_date.strftime("%d") }}'
    ) +'/',
    bucket = BUCKET_NAME,
    execution_timeout = timedelta(seconds=300),
    dag=dag,
)


upload_sales
import os
import requests
from datetime import datetime
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator


JOB1_PORT = 8081
JOB2_PORT = 8082
BASE_DIR = "../data"
RAW_DIR = os.path.join(BASE_DIR, "raw", "sales")
STG_DIR = os.path.join(BASE_DIR, "stg", "sales")



def run_job1(run_date):
    print("Starting job1:", f'http://0.0.0.0:{JOB1_PORT}/')
    resp = requests.post(
        url=f'http://0.0.0.0:{JOB1_PORT}/',
        json={
            "date": run_date,
            "raw_dir": os.path.join(RAW_DIR, run_date)
        }
    )
    assert resp.status_code == 201
    print("job1 completed!")

def run_job2(run_date):
    print("Starting job2:")
    resp = requests.post(
        url=f'http://localhost:{JOB2_PORT}/',
        json={
            "raw_dir": os.path.join(RAW_DIR, str(run_date)),
            "stg_dir": os.path.join(STG_DIR, str(run_date))
        }
    )
    assert resp.status_code == 201
    print("job2 completed!")


dag = DAG(
    dag_id='extract_convert',
    start_date=datetime(2022, 8, 9),
    end_date=datetime(2022, 8, 12),
    schedule_interval="0 1 * * *",
    catchup=True,
    max_active_runs=1,
)


task1 = PythonOperator(
    dag=dag,
    task_id='extract_data_from_api',
    python_callable=run_job1,
    op_args=["{{ ds }}"],
)

task2 = PythonOperator(
    dag=dag,
    task_id='convert_to_avro',
    python_callable=run_job2,
    op_args=["{{ ds }}"],
)

task1 >> task2

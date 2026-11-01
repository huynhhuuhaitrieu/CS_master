import uuid
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2026, 11, 1, 10, 00)
}

def stream_data(): 
    import json
    # from kafka import KafkaProducer
    import time
    import logging

    # producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    # curr_time = time.time()

    # while True:
    #     if time.time() > curr_time + 60: #1 minute
    #         break
    #     try:
    #         res = get_data()
    #         res = format_data(res)

    #         producer.send('users_created', json.dumps(res).encode('utf-8'))
    #     except Exception as e:
    #         logging.error(f'An error occured: {e}')
    #         continue
    import requests
    
    res = requests.get("https://randomuser.me/api/")
    print(res = res.json())


with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )

stream_data();
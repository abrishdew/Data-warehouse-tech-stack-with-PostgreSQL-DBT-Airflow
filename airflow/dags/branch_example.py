from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta
import pandas as pd

from airflow.utils.email import send_email



default_args = {
    'owner': 'Tenx_backend', #person or team responsible for the DAG
    'start_date': datetime(2023, 1, 1), #first execution date for the DAG
    'retries': 1, # Number of times Airflow should retry running a task in case of failure
    'retry_delay': timedelta(minutes=5), # The delay between retries
}

dag = DAG(
    'branching_example_dag',# : This is a unique identifier for the DAG within the Airflow environment
    default_args=default_args,
    description='An example DAG with branching', # : This is a description of what the DAG does
    schedule_interval='@daily', # how often the DAG should run daily, hourly, weekly,
)

def choose_branch(**kwargs):
    current_weekday = datetime.now().weekday()
    if current_weekday == 0:  # Monday is 0
        return 'monday_task'
    elif current_weekday == 3:  # Wednesday is 3
        return 'interim_task'
    elif current_weekday == 5:  # Saturday is 5
        return 'Final_task'
    else:
        return 'other_day_task'

branch_task = BranchPythonOperator( # execute different downstream tasks based on a condition evaluated at runtime
    task_id='branch_decision',
    python_callable=choose_branch,
    provide_context=True,
    dag=dag,
)

def monday_task(**kwargs):
    print("Today is Monday for challenge introduction!")
    return "Today is Monday for challenge introduction!"
    

def wednesday_day_task(**kwargs):
    print("Interim submission Task.")

def saturday_day_task(**kwargs):
    print("Final submission Task.")
def other_day_task(**kwargs):
    print("Work hard not to miss the deadline!")

monday_task = PythonOperator(
    task_id='monday_task',
    python_callable=monday_task,
    provide_context=True,
    dag=dag,
)
wednesday_day_task = PythonOperator(
    task_id='wednesday_day_task',
    python_callable=wednesday_day_task,
    provide_context=True,
    dag=dag,
)
saturday_day_task = PythonOperator(
    task_id='saturday_day_task',
    python_callable=saturday_day_task,
    provide_context=True,
    dag=dag,
)

other_day_task = PythonOperator(
    task_id='other_day_task',
    python_callable=other_day_task,
    provide_context=True,
    dag=dag,
)


def send_custom_email(**kwargs):
    ti = kwargs['ti']
    # Pull the message from the previous task's XCom
    message = ti.xcom_pull(task_ids='monday_task')

    email_content = f"<p>{message}</p>"
    send_email(to='xxxxx', subject='Airflow Alert', html_content=email_content)



email_task = EmailOperator(
    task_id='send_email',
    to='mahlet@10academy.org',
    subject='Airflow Alert',
    html_content='<p>Today is not Monday!</p>',
    dag=dag
)
branch_task >> [monday_task, wednesday_day_task, saturday_day_task, other_day_task]

branch_task >> other_day_task >> email_task
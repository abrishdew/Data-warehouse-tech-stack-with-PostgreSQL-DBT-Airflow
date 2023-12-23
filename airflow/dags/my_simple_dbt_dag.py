from pendulum import datetime
from airflow.decorators import dag
from airflow.operators.bash import BashOperator

PATH_TO_DBT_PROJECT = "/home/abresh/Desktop/CSV/airflow/dags/dbt/traffic_data"
PATH_TO_DBT_VENV = "/home/abresh/Desktop/CSV/my_env"


@dag(
    start_date=datetime(2023, 3, 23),
    schedule="@daily",
    catchup=False,
)
def simple_dbt_dag():
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="source $PATH_TO_DBT_VENV && dbt run --models .",
        env={"PATH_TO_DBT_VENV": PATH_TO_DBT_VENV},
        cwd=PATH_TO_DBT_PROJECT,
    )


simple_dbt_dag()
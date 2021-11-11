"""Example fail DAG"""
import datetime
import os

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

# setup for a local dag
args = {
    "owner": "Nano Airflow Admin",
    "catchup": False,
    "email": ["juraj.palka@nanoenergies.cz", "analytics.services@nanox.cz"],
    "email_on_failure": True,
    "email_on_retry": False,
    "depends_on_past": False,
    "start_date": datetime.datetime(2021, 11, 2, 5, 0),
    "params": {"environment": os.environ.get("AIRFLOW_ENVIRONMENT")},
}

dag = DAG(dag_id="vit_example_v1", default_args=args, schedule_interval="0 5 * * *")


def _simple_print(ts: str, **context):
    """Print context"""
    print(context)
    print(ts)

with dag:
    # Run tasks
    simple_print = PythonOperator(
        task_id="simple_print",
        python_callable=_simple_print,
        retries=2,
        retry_delay=datetime.timedelta(minutes=2),
    )

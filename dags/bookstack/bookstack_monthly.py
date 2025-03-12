from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow import DAG
from datetime import datetime

# Daily Task: Runs a shell script every midnight
with DAG(
    dag_id="bookstack_monthly",
    schedule_interval="10 4 1 * *",  # Runs daily at midnight
    start_date=datetime(2025, 1, 21),
    catchup=False,  # Prevents backfilling for missed runs
) as dag:
    run_remote_shell_script = SSHOperator(
        task_id="bookstack_monthly",
        ssh_conn_id="bookstack",
        command="{{ 'bash /home/bookstack/backup/backup_script_monthly.sh' }}",
        cmd_timeout=None,
    	execution_timeout=None,

    )


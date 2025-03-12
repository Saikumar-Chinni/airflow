from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow import DAG
from datetime import datetime

# Daily Task: Runs a shell script every midnight
with DAG(
    dag_id="bookstack_daily",
    schedule_interval="0 4 * * *",  
    start_date=datetime(2025, 1, 1),
    catchup=False,  # Prevents backfilling for missed runs
) as dag:
    run_remote_shell_script = SSHOperator(
        task_id="bookstack_daily",
        ssh_conn_id="bookstack",
        command="{{ 'bash /home/bookstack/backup/backup_script_daily.sh' }}",
        cmd_timeout=None,
    	execution_timeout=None,

    )

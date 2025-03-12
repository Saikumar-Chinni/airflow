from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow import DAG
from datetime import datetime

# Daily Task: Runs a shell script every midnight
with DAG(
    dag_id="pinacaplane_daily",
    schedule_interval="15 3 * * *",  # Runs daily at midnight
    start_date=datetime(2024, 12, 23),
    catchup=False,  # Prevents backfilling for missed runs
) as dag:
    run_remote_shell_script = SSHOperator(
        task_id="pinacaplane_daily",
        ssh_conn_id="pinacaplane",
        command="{{ 'bash /home/pinacaplane/backup/backup_script_daily.sh' }}",
	cmd_timeout=None,
    	execution_timeout=None,

    )

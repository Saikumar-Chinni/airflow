from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow import DAG
from datetime import datetime

# Monthly Task: Runs on the 1st day of every month at midnight
with DAG(
    dag_id="gitea_monthly",
    schedule_interval="10 0 1 * *",  # Runs at midnight on the 1st of every month
    start_date=datetime(2025, 1, 2),  # Start date
    catchup=False,  # Prevents backfilling for missed runs
) as dag:
    run_backup_script = SSHOperator(
        task_id="gitea_monthly",
        ssh_conn_id="gitea",  # Replace with your actual SSH connection ID
        command="{{ 'bash /home/gitea/backup/backup_script_monthly.sh' }}",  # Replace with your actual backup script path
	cmd_timeout=None,
    	execution_timeout=None,
    )

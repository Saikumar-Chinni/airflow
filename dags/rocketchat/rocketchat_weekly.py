from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow import DAG
from datetime import datetime

# Weekly Task: Runs at midnight Sunday night (technically Monday at 00:00)
with DAG(
    dag_id="rocketchat_weekly",
    schedule_interval="20 1 * * SUN",  # Runs at midnight every Sunday night
    start_date=datetime(2025, 1, 1),  # Start date (adjust as necessary)
    catchup=False,  # Prevents backfilling for missed runs
) as dag:
    run_backup_script = SSHOperator(
        task_id="rocketchat_weekly",
        ssh_conn_id="rocketchat",  # Replace with your actual SSH connection ID
        command="{{ 'bash /home/ubuntu/backup/backup_script_weekly.sh' }}",  # Replace with your actual backup script path
	cmd_timeout=None,
    	execution_timeout=None,

    )

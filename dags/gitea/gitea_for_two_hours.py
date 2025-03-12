from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow import DAG
from datetime import datetime

# Runs every 2 hours between 8 AM and 8 PM starting from the start_date
with DAG(
    dag_id="gitea_every_two_hours",
    schedule_interval="5 */2 * * *",
    start_date=datetime(2024, 12, 22),  # Start date
    catchup=False,  # Prevents backfilling for missed runs
) as dag:
    run_backup_script = SSHOperator(
        task_id="gitea_for_every_two_hours",
        ssh_conn_id="gitea",  # Replace with your actual SSH connection ID
        command="{{ 'bash /home/gitea/backup/backup_script_two_hours.sh' }}",  # Replace with your actual backup script path
        cmd_timeout=None,
        execution_timeout=None,
    )

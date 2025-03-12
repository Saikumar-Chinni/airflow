from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow import DAG
from datetime import datetime

# Daily Task: Runs a shell script every midnight
with DAG(
    dag_id="rocketchat_daily",
    schedule_interval="0 1 * * *",  # Runs daily at midnight
    start_date=datetime(2024, 12, 23),
    catchup=False,  # Prevents backfilling for missed runs
) as dag:
    run_remote_shell_script = SSHOperator(
        task_id="rocketchat_daily",
        ssh_conn_id="rocketchat",
        command="{{ 'bash /home/ubuntu/backup/backup_script_daily.sh' }}",
	cmd_timeout=None,
    	execution_timeout=None,

    )
    trigger_another_dag = TriggerDagRunOperator(
        task_id='datacopy_daily',
        trigger_dag_id='datacopy_daily',  # The ID of the DAG to trigger
    )

    run_remote_shell_script >> trigger_another_dag

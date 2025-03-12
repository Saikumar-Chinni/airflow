# Apache Airflow

Apache Airflow is an open-source workflow automation and orchestration tool used to author, schedule, and monitor workflows as Directed Acyclic Graphs (DAGs). It is widely used for data engineering, ETL processes, and machine learning pipelines.

## Features
- **Scalability**: Easily scale workflows using a distributed architecture.
- **Flexibility**: Define workflows as Python code.
- **Monitoring**: Web UI to track task execution and logs.
- **Integrations**: Supports various third-party integrations like AWS, GCP, and Kubernetes.
- **Scheduling**: Provides advanced scheduling capabilities for workflows.

## Use Cases
- **ETL (Extract, Transform, Load) Pipelines**: Automating data extraction, transformation, and loading processes.
- **Machine Learning Workflows**: Managing ML model training, evaluation, and deployment.
- **Data Warehousing**: Automating data movement and processing in data lakes and warehouses.
- **DevOps & Automation**: Automating infrastructure tasks, CI/CD pipelines, and cloud resource management.
- **Business Process Automation**: Orchestrating business workflows with dependencies.

## Installation
You can install Airflow using pip:

```bash
pip install apache-airflow
```

Or install it with constraints:

```bash
pip install 'apache-airflow==2.5.0' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.8.txt"
```

## Getting Started
1. **Initialize Airflow Database**
   ```bash
   airflow db init
   ```
2. **Create an Admin User**
   ```bash
   airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com
   ```
3. **Start the Web Server**
   ```bash
   airflow webserver --port 8080
   ```
4. **Start the Scheduler**
   ```bash
   airflow scheduler
   ```
5. **Access Airflow UI**
   Open `http://localhost:8080/` in a browser.

## Creating a DAG
A simple DAG example (`simple_dag.py`):

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, Airflow!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 12),
    'retries': 1
}

dag = DAG(
    'simple_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

task = PythonOperator(
    task_id='hello_task',
    python_callable=hello_world,
    dag=dag
)
```

Save this file in the `dags/` directory of your Airflow setup.

## Running Tasks
To trigger the DAG manually, use:
```bash
airflow dags trigger simple_dag
```

To check DAG status:
```bash
airflow dags list
```

## Conclusion
Apache Airflow is a powerful workflow orchestration tool that helps automate and manage data pipelines efficiently. It provides robust scheduling, monitoring, and extensibility, making it a popular choice for data engineers and DevOps teams.

## References
- [Official Documentation](https://airflow.apache.org/)
- [GitHub Repository](https://github.com/apache/airflow)


curl -fsSL https://get.docker.com | sh
mkdir airflow_docker
cd airflow_docker
mkdir -p ./dags ./logs ./plugins ./config
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.1/docker-compose.yaml'
sudo docker compose up airflow-init
sudo docker compose up -d





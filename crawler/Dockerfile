FROM apache/airflow:latest-python3.11

USER airflow
COPY requirements.txt /
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt

USER root
RUN apt-get update && \
    apt-get upgrade -y && \
    playwright install --with-deps
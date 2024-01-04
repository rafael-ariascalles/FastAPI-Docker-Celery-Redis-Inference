# worker.Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY celery_worker.py celery_config.py ./

CMD ["celery", "-A", "celery_worker", "worker", "--loglevel=info"]
# worker.Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY inference.py celeryconfig.py ./

CMD ["celery", "-A", "inference", "worker", "--loglevel=info"]
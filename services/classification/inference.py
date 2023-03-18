# inference.py
from time import sleep
from celery import Celery
import requests

celery_app = Celery()
celery_app.config_from_object("celeryconfig")

@celery_app.task
def long_running_task(value: int, webhook_url: str):
    # Simulate a long-running task
    sleep(value)
    result = f"Task completed after {value} seconds"
    
    # Send the result to the webhook URL
    if webhook_url:
        requests.post(webhook_url, json={"result": result})
    
    return result
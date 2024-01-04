# inference.py
from time import sleep
from celery import Celery
import requests
import os

celery_app = Celery()
celery_app.config_from_object("celery_config")

@celery_app.task(name="long_running_task")
def long_running_task(text: str, webhook_url: str):
    # Simulate a long-running task
    wait_sec = 15
    sleep(wait_sec)
    result = f"Task completed for {text} after {wait_sec} seconds"
    print(result)
    if webhook_url:
        requests.post(webhook_url, json={"result": result})
    
    return result
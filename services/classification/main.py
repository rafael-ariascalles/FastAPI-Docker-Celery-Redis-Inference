# main.py
from fastapi import FastAPI
from celery import Celery
from pydantic import BaseModel

app = FastAPI()
celery_app = Celery()
celery_app.config_from_object("celeryconfig")

class TaskInput(BaseModel):
    value: int
    webhook_url: str

@app.post("/start_task/")
async def start_task(task_input: TaskInput):
    task = celery_app.send_task(
        "inference.long_running_task", args=[task_input.value, task_input.webhook_url]
    )
    return {"task_id": task.id}

@app.get("/get_task_result/{task_id}")
async def get_task_result(task_id: str):
    task = celery_app.AsyncResult(task_id)
    if task.ready():
        return {"status": "completed", "result": task.result}
    return {"status": "in progress"}
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from celery_worker import celery_app, long_running_task

app = FastAPI()

class TaskInput(BaseModel):
    text: str 
    webhook_url: Optional[str]

@app.post("/start_task/")
async def start_task(task_input: TaskInput):
    task = long_running_task.delay(text= task_input.text, webhook_url=task_input.webhook_url)
    print(task)
    return {"task_id": task.id}

@app.get("/get_task_result/{task_id}")
async def get_task_result(task_id: str):
    task = celery_app.AsyncResult(task_id)
    print(task.result)
    if task.ready():
        return {"status": "completed", "result": task.result}
    return {"status": "in progress"}
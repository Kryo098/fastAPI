from typing import List

from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()


@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のタスク")]


@router.post("/tasks", response_model=task_schema.TaskCreateResPonse)
async def create_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResPonse(id=1, **task_body.dict())


@router.put("/tasks")
async def update_task():
    pass


@router.delete("/tasks")
async def delete_task():
    pass

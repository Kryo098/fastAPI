from typing import List

from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()


@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のタスク")]


@router.post("/tasks")
async def create_tasks():
    pass


@router.put("/tasks")
async def update_tasks():
    pass


@router.delete("/tasks")
async def delete_tasks():
    pass

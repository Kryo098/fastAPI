from fastapi import APIRouter

router = APIRouter()


@router.put("/tasks/{tasks_id}/done")
async def mark_task_as_done(task_id: int):
    return


@router.delete("/tasks/{tasks_id}/done")
async def unmark_task_as_done(task_id: int):
    return

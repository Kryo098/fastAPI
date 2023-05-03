from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
async def list_tasks():
    pass


@router.post("/tasks")
async def create_tasks():
    pass


@router.put("/tasks")
async def update_tasks():
    pass


@router.delete("/tasks")
async def delete_tasks():
    pass

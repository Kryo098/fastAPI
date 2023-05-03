from typing import Optional

from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="洗濯物を取り込む")
    done: bool = Field(False, description="完了フラグ")
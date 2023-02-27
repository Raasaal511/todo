from pydantic import BaseModel


class BaseTodo(BaseModel):
    id: int
    title: int
    complate: bool

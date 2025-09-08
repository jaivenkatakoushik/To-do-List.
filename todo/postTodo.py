from fastapi import APIRouter
from pydantic import BaseModel

router=APIRouter()

class TodoModel(BaseModel):
  name: str
  done: bool
  # des: str | None=None

todo={}

@router.post('/todo/create')
def create_todo(item : TodoModel):
  id=int(len(todo)+1)
  todo[id]=item.dict()
  return {id:todo[id]}
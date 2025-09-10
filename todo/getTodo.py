from fastapi import APIRouter
from .postTodo import todo

router=APIRouter()

@router.get('/todo')
def read_all_todos():
  to={}
  for i in todo:
    temp=todo[i]['name']
    to[temp]={'done':todo[i]['done']}
  return to

@router.get('/todo/filter/')
def read_by_range(status:bool =None,start:int =None,end:int =None):
  if(end==None):
      end=len(todo)
  if(start==None):
    start=1
  if(start>end or start<=0 or end<=0 or end>len(todo)):
    return {'Wrong Selection':'Please'}
  to={}
  if(status==None):
    for i in range(start,end+1):
      temp=todo[i]['name']
      to[temp]=todo[i]['done']
  else:
    for i in range(start,end+1):
      if todo[i]['done']==status:
        temp=todo[i]['name']
        to[temp]=todo[i]['done']
  return to

@router.get('/todo/getById/{id}')
def read_by_id(id:int =None):
  for i in todo:
    if i==id:
      return todo[i]
  return {'error':'There is No record'}

@router.get('/todo/getByName/{name}')
def read_by_name(name: str=None):
  if(name==None):
    return {'error':'Select a Name'}
  for i in todo:
    if(todo[i]['name']==name):
      return { todo[i]['name']:todo[i]['done'] }
  return {'error':'There is No such data'}
from fastapi import APIRouter

router=APIRouter()

todo={
  1:{
    'name':'Task-1',
    'done':True
  },
  2:{
    'name':'Task-2',
    'done':False
  }
}

@router.get('/todo')
def read_all_todos():
  to={}
  for i in todo:
    temp=todo[i]['name']
    to[temp]={'done':todo[i]['done']}
  return to

@router.get('/todo/filter/range')
def read_by_range(start:int =None,end:int =None):
  if((start==None and end==None) or start>end or start<0 or end<0 or end>len(todo)):
    return {'error':'Select Correct Number'}
  if(end==None):
    end=len(todo)
  if(start==None):
    start=1
  to={}
  for i in range(start,end+1):
    temp=todo[i]['name']
    to[temp]=todo[i]['done']
  return to

@router.get('/todo/{id}')
def read_by_id(id:int =None):
  for i in todo:
    if i==id:
      return todo[i]
  return {'error':'There is No record'}


@router.get('/todo/status/{done}')
def read_by_value(done:bool =True):
  if(done.lower()!='true' and done.lower()!='false'):
    return {'error':'wrong Selection'}
  if(done.lower()=='true'):
    done=True
  if(done.lower()=='false'):
    done=False
  to={}
  for i in todo:
    if(todo[i]['done']==done):
      temp=todo[i]['name']
      to[temp]=todo[i]['done']
  return to

@router.get('/todo/filter/getByName/{name}')
def read_by_name(name: str=None):
  if(name==None):
    return {'error':'Select a Name'}
  for i in todo:
    if(todo[i]['name']==name):
      return { todo[i]['name']:todo[i]['done'] }
  return {'error':'There is No such data'}
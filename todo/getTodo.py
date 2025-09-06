from fastapi import APIRouter

router=APIRouter()

todo={
  '1':{
    'name':'Task-1',
    'done':'true'
  },
  '2':{
    'name':'Task-2',
    'done':'false'
  }
}

@router.get('/todo')
def read_all_todos():
  to={}
  for i in todo:
    temp=todo[i]['name']
    to[temp]={'done':todo[i]['done']}
  return to

@router.get('/todo/{id}')
def read_by_id(id:str =None):
  for i in todo:
    if i==id:
      return todo[i]
  return {'error':'There is No record'}

@router.get('/todo/status/{done}')
def read_all_true(done:str ='true'):
  if(done.lower()!='true' and done.lower()!='false'):
    return {'error':'wrong Selection'}
  to={}
  for i in todo:
    if(todo[i]['done']==done.lower()):
      temp=todo[i]['name']
      to[temp]=todo[i]['done']
  return to


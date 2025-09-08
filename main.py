from fastapi import FastAPI
from todo import getTodo
from todo import postTodo

app = FastAPI()

app.include_router(getTodo.router)
app.include_router(postTodo.router)

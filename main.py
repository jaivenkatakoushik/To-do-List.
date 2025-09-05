from fastapi import FastAPI

app = FastAPI()

k={1: "one", 2: "two",3: "three",4: "four",5: "five"}

@app.get("/")
def read_root():
    return {"First": "API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str =""):
    q=k[item_id]
    return {"item_id": item_id, "q": q}
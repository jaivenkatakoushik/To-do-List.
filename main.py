from fastapi import FastAPI

app = FastAPI()

k={1: "one", 2: "two",3: "three",4: "four",5: "five"}

@app.get("/")
def read_root():
    return {"First": "API"}
@app.get("/items/")
def read_all_items():
    return {"items": k}

@app.get("/items/even")
def read_even_items():
    even={}
    for i in list(k.keys()):
        if i%2 ==0:
            even[i]=k[i]
    return {"even_items": even}

@app.get("/items/odd")
def read_odd_items():
    odd={}
    for i in list(k.keys()):
        if i%2 !=0:
            odd[i]=k[i]
    return {"odd_items": odd}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str =""):
    q=k[item_id]
    return {"item_id": item_id, "q": q}
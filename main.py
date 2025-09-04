import fastapi as fastapi

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"First": "API"}
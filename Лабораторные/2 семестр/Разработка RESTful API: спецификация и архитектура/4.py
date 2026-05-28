from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item_by_path(item_id: int):
    return {
        "method": "path",
        "item_id": item_id
    }

@app.get("/items")
def get_item_by_query(item_id: int):
    return {
        "method": "query",
        "item_id": item_id
    }
#  fastapi is file name and FastAPI class 
from fastapi import FastAPI
import db
import model

# app is object of FastAPI
app = FastAPI()

@app.get("/all")
def get_all():
    data = db.all()
    return {"data": data}

@app.post("/create")
def create(data: model.Todo):
    id = db.create(data)
    return {"inserted": True,"inserted_id": id}

@app.get("/get/{name}")
def get_one(name: str):
    data = db.get_one(name)
    return {"data": data}

@app.delete("/delete")
def delete(name: str):
    data = db.delete(name)
    return {"deleted": True, "deleted_count": data}

@app.put("/update")
def update(data: model.Todo):
    data = db.update(data)
    return {"updated": True, "updated_count": data}


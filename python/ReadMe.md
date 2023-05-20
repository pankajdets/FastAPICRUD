pip install fastapi

to run: auto refresh

python -m uvicorn main:app --reload

**HTTP Get Method**

    @app.get("/home")
    async def root():
        return {"message": "Hello World"}

**Path Parameters**
    @app.get("/items/{item_id}")
    async def read_item(item_id: int):
        return {"item_id": item_id}

    **default**

        fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


        @app.get("/items/")
        async def read_item(skip: int = 0, limit: int = 10):
            return fake_items_db[skip : skip + limit]

    **Optional**

        @app.get("/items/{item_id}")
        async def read_item(item_id: str, q: str | None = None):
            if q:
                return {"item_id": item_id, "q": q}
            return {"item_id": item_id}

    ****
**Query Parameters**

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

    @app.get("/items/")
    async def read_item(item_id: int):
        return {"item_id": item_id}

**HTTP POST Method ---Request Body**

b = {}
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    db["name"] = item.name
    db["description"] = item.description
    db["price"] = item.price
    db["tax"] = item.tax
    return {"item Saved": item.name}



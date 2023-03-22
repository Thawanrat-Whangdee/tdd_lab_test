from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel 

app = FastAPI()

Class Name(BaseModel):    
   name : str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.post("/callname")
def read_name(request: Name):
   data : {
      'name': request.name,
   }
   return {"hello": data}

handler = Mangum(app)

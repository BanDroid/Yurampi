from typing import Union

from fastapi import FastAPI
from dotenv import load_dotenv
from config.lifespan import lifespan
from routes.router import router as api_router

load_dotenv()

app = FastAPI(lifespan=lifespan)


@app.get("/")
def root_path():
    return {"Lu": "Kontol"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = "hello world"):
    if q == "":
        return {"item_id": item_id, "q": "q is empty"}
    return {"item_id": item_id, "q": q}


app.include_router(api_router, prefix="/api")

from typing import Union
from fastapi import FastAPI, Depends
from fastapi_health import health

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def get_session():
    return True

def is_database_online(session: bool = Depends(get_session)):
    return session


app.add_api_route("/health", health([is_database_online]))
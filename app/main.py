from fastapi import FastAPI
from pydantic import BaseModel
from app.db import database, User


app = FastAPI()


class Message(BaseModel):
    message: str | None = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/echo/{message}")
async def read_item(message: str):
    return {"message": message}


@app.post("/echo")
async def write_item(message: Message):
    return message


@app.get("/users")
async def read_root():
    return await User.objects.all()


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com", password="test", firstname="test", lastname="test")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()

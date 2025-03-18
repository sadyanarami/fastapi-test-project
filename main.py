from random import randint
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    return {"massage": "Hello world!"}

@app.get("/pool")
async def pool():
    rand_num = randint(0, 10)
    return {"pool": rand_num}

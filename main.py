from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    return {"massage": "Hello world!"}

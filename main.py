from fastapi import FastAPI

from config import load_config
from logger import logger
from models import Feedback, User


app = FastAPI()

config = load_config()
if config.debug:
    app.debug = True
else:
    app.debug = False


@app.get("/")
def read_root():
    logger.info("Handling request to root endpoint")
    return {"message": "Hello, World!"}


@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return {"database_url": config.db.database_url}


user = User(id=1, name="John Doe", age=20)


@app.get("/users")
def get_users():
    return {"name": user.name, "id": user.id}


@app.post("/user")
def is_adult(user: User):
    if user.age > 18:
        return {"name": user.name, "age": user.age, "is_adult": True}
    else:
        return {"name": user.name, "age": user.age, "is_adult": False}

fake_db_feedback = []

@app.post("/feedback")
def feedback(feedback: Feedback):
    fake_db_feedback.append({
        "name": feedback.name,
        "comments": feedback.message
    })
    return {"message": f"Feedback received. Thank you, {feedback.name}!"}

# Доделать нужно!!! тут короче я хочу чтобы когда пишешь нейм выдавал его фидбек и его никнейм
@app.get("/comments/{name}")
def comments(name: str = None, limit: int = 10):
    return fake_db_feedback[:limit]

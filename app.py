from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User, Feedback
from feedback_data import feedbacks

application = FastAPI()

#1.1
@application.get("/")
async def read_root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

#1.2
@application.get("/index", response_class=FileResponse)
async def get_html_page():
    return "index.html"

#1.4
@application.get("/users", response_model=User)
async def get_user():
    example_user = User(name="Семенов Тихон", id=1)
    return example_user

#2.1
@application.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}
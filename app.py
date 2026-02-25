from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from models import User, Feedback
from feedback_data import feedbacks

application = FastAPI()

@application.get("/")
async def read_root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

@application.get("/index", response_class=FileResponse)
async def get_html_page():
    return "index.html"

@application.get("/users", response_model=User)
async def get_user():
    example_user = User(name="Ваше Имя и Фамилия", id=1)
    return example_user

@application.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    
    return {"message": f"Feedback received. Thank you, {feedback.name}."}
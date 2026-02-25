from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User

application = FastAPI()

@application.get("/")
async def read_root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

@application.get("/index", response_class=FileResponse)
async def get_html_page():
    return "index.html"

@application.get("/users", response_model=User)
async def get_user():
    """
    Returns a JSON representation of a User.
    """
    example_user = User(name="Ваше Имя и Фамилия", id=1)  # Replace with your actual name
    return example_user
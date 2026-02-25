from fastapi import FastAPI
from fastapi.responses import FileResponse

application = FastAPI()

@application.get("/")
async def read_root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

@application.get("/index", response_class=FileResponse)
async def get_html_page():
    return "index.html"
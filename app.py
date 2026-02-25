from fastapi import FastAPI

application = FastAPI()

@application.get("/")
async def read_root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}
from pydantic import BaseModel
#1.4
class User(BaseModel):
    name: str
    id: int
#2.1
class Feedback(BaseModel):
    name: str
    message: str
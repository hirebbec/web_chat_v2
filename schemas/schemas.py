from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str


class Message(BaseModel):
    id: int
    content: str
    timestamp: datetime
    sender_id: int


class Login(BaseModel):
    username: str
    password: str

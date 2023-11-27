from datetime import datetime
from typing import List

from pydantic import BaseModel


class GetUser(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str


class CreateUser(BaseModel):
    username: str
    password: str


class GetMessage(BaseModel):
    id: int
    content: str
    timestamp: datetime
    sender_id: int


class CreateMessage(BaseModel):
    content: str
    sender_id: int


class GetMessages(BaseModel):
    messages: List[GetMessage]

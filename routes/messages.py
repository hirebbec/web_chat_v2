from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import get_db
from schemas.schemas import Message
from service import message_service

message_router = APIRouter(prefix="/message", tags=["messages"])


@message_router.get("/")
async def get_all_messages(service: MessageService = Depends()):
    return message_service.get_all(db)


@message_router.post("/")
async def create_message(content: str, sender_id: int, db: Session = Depends(get_db)):
    return message_service.create(content, sender_id, db)


@message_router.get("/{id}")
async def get_message_by_id(id: int, db: Session = Depends(get_db)):
    return message_service.get(id, db)


@message_router.get('/{user_id}')
async def get_user_messages(user_id: int):
    pass

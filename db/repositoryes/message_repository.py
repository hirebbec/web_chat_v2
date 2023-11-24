from typing import Type

from fastapi import Depends
from sqlalchemy.orm import Session

from db.db import get_db
from db.models import Message
from schemas.schemas import CreateMessage


class MessageRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self._session = session

    def create_message(self, message: CreateMessage) -> Message:
        new_message = Message(content=message.content, sender_id=message.sender_id)
        self._session.add(new_message)
        self._session.commit()
        self._session.refresh(new_message)
        return new_message

    def get_message(self, id: int) -> Message | None:
        return self._session.query(Message).filter(Message.id == id).first()

    def get_all_messages(self) -> list[Message]:
        return self._session.query(Message).all()

    def delete(self, id: int) -> None:
        user = self._session.query(Message).filter(Message.id == id).first()
        self._session.delete(user)
        self._session.commit()

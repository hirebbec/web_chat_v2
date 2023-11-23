from typing import Type

from fastapi import Depends
from sqlalchemy.orm import Session

from db.models import Message


class MessageRepository():
    def __init__(self, session: Session = Depends()):
        self._session = session

    def create_message(self, content: str, sender_id: int):
        new_message = Message(content=content, sender_id=sender_id)
        self._session.add(new_message)
        self._session.commit()
        self._session.refresh(new_message)
        return new_message

    def get_message(self, id: int):
        return self._session.query(Message).filter(Message.id == id).first()

    def get_all_messages(self) -> list[Type[Message]]:
        return self._session.query(Message).all()

    # def get_user_by_username(db: Session, username: str):
    #     return db.query(User).filter(User.username == username).first()
    #
    #
    # def update_user(db: Session, id: int, data: dict):
    #     user = db.query(User).filter(User.id == id).first()
    #     for key, value in data.items():
    #         setattr(user, key, value)
    #     db.commit()
    #     db.refresh(user)
    #     return user
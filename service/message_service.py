from fastapi import Depends

from db.messages import *
from db.repositoryes.message_repository import MessageRepository


class MessageService:

    def __init__(self, message_repository: MessageRepository = Depends()):
        self._message_repository = message_repository
def create(self, content: str, sender_id: int):
    return self._message_repository.create_message(content, sender_id)

def get(self, id :int, db: Session):
    return self._message_repository.get_message(id, db)

def get_all(self, db: Session):
    return self._message_repository.get_all_messages(db)
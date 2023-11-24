from typing import Type

from fastapi import Depends

from db.models import Message
from db.repositoryes.message_repository import MessageRepository
from schemas.schemas import CreateMessage


class MessageService:
    def __init__(self, message_repository: MessageRepository = Depends()):
        self._message_repository = message_repository

    def create(self, message: CreateMessage):
        return self._message_repository.create_message(message)

    def get(self, id: int):
        return self._message_repository.get_message(id)

    def get_all(self) -> list[Message]:
        return self._message_repository.get_all_messages()

    def delete(self, id: int):
        return self._message_repository.delete(id)

from fastapi import APIRouter, Depends

from schemas.schemas import CreateMessage
from service.message_service import MessageService

message_router = APIRouter(prefix="/message", tags=["messages"])


@message_router.get("/")
async def get_all_messages(service: MessageService = Depends()):
    return service.get_all()


@message_router.post("/")
async def create_message(message: CreateMessage, service: MessageService = Depends()):
    return service.create(message)


@message_router.get("/{id}")
async def get_message_by_id(id: int, service: MessageService = Depends()):
    return service.get(id)


@message_router.delete("/{id}")
async def delete_message(id: int, service: MessageService = Depends()):
    return service.delete(id)

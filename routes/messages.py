from fastapi import APIRouter, Depends
from service.message_service import MessageService


message_router = APIRouter(prefix="/message", tags=["messages"])


@message_router.get("/")
async def get_all_messages(service: MessageService = Depends()):
    return service.get_all()


@message_router.post("/")
async def create_message(content: str, sender_id: int, service: MessageService = Depends()):
    return service.create(content, sender_id)


@message_router.get("/{id}")
async def get_message_by_id(id: int, service: MessageService = Depends()):
    return service.get(id)


@message_router.get('/{user_id}')
async def get_user_messages(user_id: int):
    pass

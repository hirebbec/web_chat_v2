from fastapi import APIRouter

from schemas.schemas import User, Message

message_router = APIRouter(prefix="/message", tags=["messages"])


@message_router.get("/")
async def get_all_messages():
    pass


@message_router.post("/")
async def create_message(msg: Message):
    pass


@message_router.get("/{id}")
async def get_message_by_id(id: int):
    pass


@message_router.get('/{user_id}')
async def get_user_messages(user_id: int):
    pass

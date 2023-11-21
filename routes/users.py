from fastapi import APIRouter
from schemas.schemas import User

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/")
async def get_all_users():
    pass


@users_router.post("/")
async def create_user(user: User):
    pass


@users_router.get("/{id}")
async def get_user_by_id(id: int):
    pass

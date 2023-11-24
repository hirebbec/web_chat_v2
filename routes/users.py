from typing import List, Type

from fastapi import APIRouter, Depends

from db.models import User
from schemas.schemas import CreateUser
from service.users_service import UserService

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/")
async def get_all_users(service: UserService = Depends()) -> List[User]:
    return service.get_all()


@users_router.post("/")
async def create_user(user: CreateUser, service: UserService = Depends()):
    return service.create(user)


@users_router.get("/{id}")
async def get_by_id(id: int, service: UserService = Depends()):
    return service.get(id)


@users_router.delete("/{id}")
async def delete_users_by_id(id: int, service: UserService = Depends()):
    return service.delete(id)

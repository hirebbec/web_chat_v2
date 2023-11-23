from fastapi import APIRouter, Depends
from schemas.schemas import Login
from service.users_service import UserService

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/")
async def get_all_users(service: UserService = Depends()):
    return service.get_all()


@users_router.post("/")
async def create_user(data: Login, service: UserService = Depends()):
    return service.create(data)


@users_router.get("/{id}")
async def get_user_by_id(id: int, service: UserService = Depends()):
    return service.get(id)

@users_router.delete("/{id}")
async def delete_users_by_id(id: int, service: UserService = Depends()):
    return service.delete(id)

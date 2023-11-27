from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from schemas.schemas import CreateUser
from service.autorization_service import AuthorizationService

authorization_router = APIRouter()


@authorization_router.post("/register", tags=["authorization"])
async def register(
    form_data: CreateUser, service: AuthorizationService = Depends()
) -> JSONResponse:
    return service.register(form_data)


@authorization_router.post("/login", tags=["authorization"])
async def login_route(
    form_data: CreateUser, service: AuthorizationService = Depends()
) -> JSONResponse:
    return service.login(form_data)


@authorization_router.post("/chat/", tags=["authorization"])
async def chat():
    pass

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import get_db
from schemas.schemas import Login
from service import service

api_router = APIRouter()


@api_router.post("/register/")
async def register_post(form_data: Login, db: Session = Depends(get_db)):
    return service.register(form_data, db)


@api_router.post("/login/")
async def login_route(login: Login, db: Session = Depends(get_db)):
    return service.login(login.username, login.password, db)


@api_router.post("/chat/")
async def chat(db: Session = Depends(get_db)):
    pass

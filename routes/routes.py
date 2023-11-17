from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from schemas.schemas import Login
from service import service
from db.utils import get_db

api_router = APIRouter(prefix="/OpenChat")
templates = Jinja2Templates(directory="templates")

@api_router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@api_router.post("/login/")
async def login_route(login: Login, db: Session = Depends(get_db)):
    return service.login(login.username, login.password, db)


@api_router.post("/register/")
async def register(username: str, password: str, db: Session = Depends(get_db)):
    return service.register(username, password, db)

@api_router.get("/chat/")
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@api_router.post("/chat/")
async def chat(db: Session = Depends(get_db)):
    pass
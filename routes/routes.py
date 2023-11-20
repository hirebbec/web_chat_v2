from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

from schemas.schemas import Login
from service import service
from db.utils import get_db
from utils.utils import get_current_user

api_router = APIRouter(prefix="/OpenChat")
templates = Jinja2Templates(directory="templates")

@api_router.get("/login/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@api_router.post("/login/")
async def login_route(login: Login, db: Session = Depends(get_db)):
    return service.login(login.username, login.password, db)


@api_router.get("/register/")
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@api_router.post("/register/")
async def register(form_data: Login, db: Session = Depends(get_db)):
    return service.register(form_data, db)


@api_router.get("/chat/", response_class=HTMLResponse)
async def chat_page(request: Request, current_user: str = Depends(get_current_user)):
    if not current_user:
        return RedirectResponse(url="/OpenChat/login")
    return templates.TemplateResponse("chat.html", {"request": request, "current_user": current_user})


@api_router.post("/chat/")
async def chat(db: Session = Depends(get_db)):
    pass


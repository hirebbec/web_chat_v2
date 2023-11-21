from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from utils.utils import get_current_user
from starlette.templating import Jinja2Templates

templates_router = APIRouter()
templates = Jinja2Templates(directory="templates")
@templates_router.get("/login/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@templates_router.get("/register/")
async def register_get(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@templates_router.get("/chat/", response_class=HTMLResponse)
async def chat_page(request: Request, current_user: str = Depends(get_current_user)):
    if not current_user:
        return RedirectResponse(url="/OpenChat/login")

    return templates.TemplateResponse(
        "chat.html", {"request": request, "current_user": current_user}
    )

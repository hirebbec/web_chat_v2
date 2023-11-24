from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse, Response
from starlette.templating import Jinja2Templates

from utils.utils import get_current_user

templates_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@templates_router.get("/login", tags=["templates"])
async def login_page(request: Request) -> Response:
    return templates.TemplateResponse("login.html", {"request": request})


@templates_router.get("/register", tags=["templates"])
async def register_get(request: Request) -> Response:
    return templates.TemplateResponse("register.html", {"request": request})


@templates_router.get("/chat", tags=["templates"])
async def chat_page(
    request: Request, current_user: dict = Depends(get_current_user)
) -> Response:
    if not current_user:
        return RedirectResponse(url="/OpenChat/login")

    return templates.TemplateResponse(
        "chat.html",
        {
            "request": request,
            "username": current_user["username"],
            "id": current_user["id"],
        },
    )

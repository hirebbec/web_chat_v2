from fastapi import APIRouter
from routes.api import api_router
from routes.templates import templates_router
from routes.users import users_router
from routes.messages import message_router

router = APIRouter(prefix="/OpenChat")

router.include_router(users_router)
router.include_router(message_router)
router.include_router(api_router)
router.include_router(templates_router)


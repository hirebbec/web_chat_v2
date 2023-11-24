from fastapi import APIRouter

from routes.authorization import authorization_router
from routes.messages import message_router
from routes.templates import templates_router
from routes.users import users_router

router = APIRouter(prefix="/OpenChat")

router.include_router(users_router)
router.include_router(message_router)
router.include_router(authorization_router)
router.include_router(templates_router)

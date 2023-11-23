from fastapi import APIRouter

from routes.messages import message_router
from routes.users import users_router

router = APIRouter(prefix="/OpenChat")

router.include_router(users_router)
router.include_router(message_router)
# router.include_router(api_router)
# router.include_router(templates_router)


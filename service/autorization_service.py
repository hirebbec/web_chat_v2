from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse

from db.db import get_db
from db.models import User
from schemas.schemas import CreateUser
from service.users_service import UserService
from utils.utils import create_access_token, hash_password_sha256, verify_pass


class AuthorizationService:
    def __init__(
        self, service: UserService = Depends(), session: Session = Depends(get_db)
    ):
        self._service = service
        self._session = session

    def save(self, form_data: CreateUser) -> User:
        new_user = User(
            username=form_data.username,
            hashed_password=hash_password_sha256(form_data.password),
        )
        self._session.add(new_user)
        self._session.commit()
        self._session.refresh(new_user)
        return new_user

    def register(self, form_data: CreateUser) -> JSONResponse:
        new_user = self.save(form_data)

        access_token = create_access_token(
            data={"username": new_user.username, "id": new_user.id}
        )
        response = JSONResponse(
            content={"access_token": access_token, "token_type": "bearer"}
        )
        response.set_cookie(key="access_token", value=access_token)

        return response

    def login(self, form_data: CreateUser) -> JSONResponse:
        user = self._service.get_by_username(form_data.username)
        if not user or not verify_pass(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )

        access_token = create_access_token(
            data={"username": user.username, "id": user.id}
        )

        return JSONResponse(
            content={
                "access_token": access_token,
                "username": user.username,
                "redirect_url": "/OpenChat/chat",
            }
        )

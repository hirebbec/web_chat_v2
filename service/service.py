from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import RedirectResponse

from db import crud
from utils.utils import verify_pass, create_access_token, hash_password_sha256


def register(username: str, password: str, db: Session):
    hashed_password = hash_password_sha256(password)
    new_user = crud.create_user(db, username, hashed_password)
    access_token = create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


def login(username: str, password: str, db: Session):
    user = crud.get_user_by_username(db, username)
    if not user or not verify_pass(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.username})

    response = RedirectResponse(url="/OpenChat/chat", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=access_token)

    return response

from typing import List, Type

from fastapi import Depends
from sqlalchemy.orm import Session

from db.db import get_db
from db.models import User


class UsersRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self._session = session

    def create_user(self, username: str, hashed_password: str) -> User:
        new_user = User(username=username, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        self._session.refresh(new_user)
        return new_user

    def get_user(self, id: int) -> User | None:
        return self._session.query(User).filter(User.id == id).first()

    def get_by_username(self, username: str) -> Type[User] | None:
        return self._session.query(User).filter(User.username == username).first()

    def update_user(self, id: int, data: dict) -> User | None:
        user = self._session.query(User).filter(User.id == id).first()
        for key, value in data.items():
            setattr(user, key, value)
        self._session.commit()
        self._session.refresh(user)
        return user

    def delete_user(self, id: int) -> None:
        user = self._session.query(User).filter(User.id == id).first()
        self._session.delete(user)
        self._session.commit()

    def get_all_users(self) -> List[User]:
        return self._session.query(User).all()

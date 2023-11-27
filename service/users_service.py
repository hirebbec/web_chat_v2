from typing import List, Type

from fastapi import Depends

from db.models import User
from db.repositoryes.user_repository import UsersRepository
from schemas.schemas import CreateUser
from utils.utils import hash_password_sha256


class UserService:
    def __init__(self, users_repository: UsersRepository = Depends()):
        self._users_repository = users_repository

    def create(self, user: CreateUser) -> User:
        hashed_password = hash_password_sha256(user.password)
        return self._users_repository.create_user(user.username, hashed_password)

    def get(self, id: int) -> User | None:
        return self._users_repository.get_user(id)

    def get_all(self) -> List[User]:
        return self._users_repository.get_all_users()

    def delete(self, id: int) -> None:
        return self._users_repository.delete_user(id)

    def get_by_username(self, username: str) -> Type[User] | None:
        return self._users_repository.get_by_username(username)

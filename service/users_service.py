from fastapi import Depends

from db.repositoryes.user_repository import UsersRepository
from schemas.schemas import Login
from utils.utils import hash_password_sha256


class UserService:
    def __init__(
            self,
            users_repository: UsersRepository = Depends()):
        self._users_repository = users_repository
    def create(self, data: Login):
        hashed_password = hash_password_sha256(data.password)
        new_user = self._users_repository.create_user(data.username, hashed_password)
        return new_user

    def get(self, id: int):
        return self._users_repository.get_user(id)

    def get_all(self):
        return self._users_repository.get_all_users()

    def delete(self, id: int):
        return self._users_repository.delete_user(id)

from fastapi import Depends
from sqlalchemy.orm import Session


class MessageRepository():
    def __init__(self, session: Session = Depends()):
        self._session = session
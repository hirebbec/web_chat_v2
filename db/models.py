from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    username: Mapped[str] = Column(String, unique=True, index=True)
    email: Mapped[str] = Column(String, unique=True, index=True)
    hashed_password: Mapped[str] = Column(String)


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    content: Mapped[str] = Column(String)
    timestamp: Mapped[datetime] = Column(DateTime, default=datetime.utcnow)
    sender_id: Mapped[int] = Column(Integer, ForeignKey("users.id"))
    sender: Mapped[User] = relationship("User", foreign_keys=[sender_id])

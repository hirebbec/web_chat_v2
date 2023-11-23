from typing import Type

from sqlalchemy.orm import Session

from db.models import Message


def create_message(content: str,  sender_id: int, db: Session):
    new_message = Message(content=content, sender_id=sender_id)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message


def get_message(id: int, db: Session):
    return db.query(Message).filter(Message.id == id).first()


def get_all_messages(db: Session) -> list[Type[Message]]:
    return db.query(Message).all()

# def get_user_by_username(db: Session, username: str):
#     return db.query(User).filter(User.username == username).first()
#
#
# def update_user(db: Session, id: int, data: dict):
#     user = db.query(User).filter(User.id == id).first()
#     for key, value in data.items():
#         setattr(user, key, value)
#     db.commit()
#     db.refresh(user)
#     return user


# def delete_user(db: Session, id: int):
#     user = db.query(User).filter(User.id == id).first()
#     db.delete(user)
#     db.commit()

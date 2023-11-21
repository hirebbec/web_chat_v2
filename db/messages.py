from sqlalchemy.orm import Session

from db.models import Message


def create_message(db: Session, content: str,  sender_id: int):
    new_message = Message(content, sender_id)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message


# def get_user(db: Session, id: int):
#     return db.query(User).filter(User.id == id).first()
#
#
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

from sqlalchemy.orm import Session
from db.models import User


def create_user(db: Session, username: str, hashed_password: str):
    new_user = User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def update_user(db: Session, id: int, data: dict):
    user = db.query(User).filter(User.id == id).first()
    for key, value in data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
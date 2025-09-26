from sqlalchemy.orm import Session
from models import User
from typing import cast, Optional


class UserRepository:

    @staticmethod
    def create(session: Session, user: User):
        with session.begin():
            session.add(user)
            session.flush()
            session.refresh(user)
        return user

    @staticmethod
    def get_by_id(session: Session, user_id: int):
        user = cast(Optional[User], session.get(User, user_id))
        return user

    @staticmethod
    def get_all(session: Session):
        return session.query(User).all()

    @staticmethod
    def get_by_role(session: Session, role_id: int):
        return session.query(User).filter(User.role_id == role_id).all()

    @staticmethod
    def get_by_email(session: Session, email: str):
        return session.query(User).filter(User.email == email).first()

    @staticmethod
    def update(session: Session, user_id: int, **kwargs):
        with session.begin():
            user = cast(Optional[User], session.get(User, user_id))
            if not user:
                return None
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            session.flush()
            session.refresh(user)
        return user

    @staticmethod
    def delete(session: Session, user_id: int):
        with session.begin():
            user = cast(Optional[User], session.get(User, user_id))
            if not user:
                return False
            session.delete(user)
        return True

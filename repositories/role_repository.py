from sqlalchemy.orm import Session
from models import Role
from typing import cast, Optional


class RoleRepository:

    @staticmethod
    def create(session: Session, role: Role):
        with session.begin():
            session.add(role)
            session.flush()
            session.refresh(role)
        return role

    @staticmethod
    def get_by_id(session: Session, role_id: int):
        role = cast(Optional[Role], session.get(Role, role_id))
        return role

    @staticmethod
    def get_all(session: Session):
        return session.query(Role).all()

    @staticmethod
    def get_by_name(session: Session, role_name: str):
        return session.query(Role).filter(Role.role_name == role_name).all()

    @staticmethod
    def update(session: Session, role_id: int, **kwargs):
        with session.begin():
            role = cast(Optional[Role], session.get(Role, role_id))
            if not role:
                return None
            for key, value in kwargs.items():
                if hasattr(role, key):
                    setattr(role, key, value)
            session.flush()
            session.refresh(role)
        return role

    @staticmethod
    def delete(session: Session, role_id: int):
        with session.begin():
            role = cast(Optional[Role], session.get(Role, role_id))
            if not role:
                return False
            session.delete(role)
        return True

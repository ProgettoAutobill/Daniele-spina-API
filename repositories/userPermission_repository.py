from sqlalchemy.orm import Session
from models import UserPermission
from typing import cast, Optional


class UserPermissionRepository:

    @staticmethod
    def create(session: Session, permission: UserPermission):
        with session.begin():
            session.add(permission)
            session.flush()
            session.refresh(permission)
        return permission

    @staticmethod
    def get_by_id(session: Session, permission_id: int):
        permission = cast(Optional[UserPermission], session.get(UserPermission, permission_id))
        return permission

    @staticmethod
    def get_all(session: Session):
        return session.query(UserPermission).all()

    @staticmethod
    def get_by_role_level(session: Session, role_level: int):
        return session.query(UserPermission).filter(UserPermission.required_role_level == role_level).all()

    @staticmethod
    def get_by_name(session: Session, name: str):
        return session.query(UserPermission).filter(UserPermission.permission_name == name).first()

    @staticmethod
    def update(session: Session, permission_id: int, **kwargs):
        with session.begin():
            permission = cast(Optional[UserPermission], session.get(UserPermission, permission_id))
            if not permission:
                return None
            for key, value in kwargs.items():
                if hasattr(permission, key):
                    setattr(permission, key, value)
            session.flush()
            session.refresh(permission)
        return permission

    @staticmethod
    def delete(session: Session, permission_id: int):
        with session.begin():
            permission = cast(Optional[UserPermission], session.get(UserPermission, permission_id))
            if not permission:
                return False
            session.delete(permission)
        return True

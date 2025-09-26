from sqlalchemy.orm import Session
from models import KeycloakSession
from typing import cast, Optional


class KeycloakSessionRepository:

    @staticmethod
    def create(session: Session, keycloak_session: KeycloakSession):
        with session.begin():
            session.add(keycloak_session)
            session.flush()
            session.refresh(keycloak_session)
        return keycloak_session

    @staticmethod
    def get_by_id(session: Session, session_id_int: int):
        keycloak_session = cast(Optional[KeycloakSession], session.get(KeycloakSession, session_id_int))
        return keycloak_session

    @staticmethod
    def get_all(session: Session):
        return session.query(KeycloakSession).all()

    @staticmethod
    def get_by_user(session: Session, user_id: int):
        return session.query(KeycloakSession).filter(KeycloakSession.user_id == user_id).all()

    @staticmethod
    def get_by_session_hash(session: Session, session_hash: str):
        return session.query(KeycloakSession).filter(KeycloakSession.session_id == session_hash).all()

    @staticmethod
    def update(session: Session, session_id_int: int, **kwargs):
        with session.begin():
            keycloak_session = cast(Optional[KeycloakSession], session.get(KeycloakSession, session_id_int))
            if not keycloak_session:
                return None
            for key, value in kwargs.items():
                if hasattr(keycloak_session, key):
                    setattr(keycloak_session, key, value)
            session.flush()
            session.refresh(keycloak_session)
        return keycloak_session

    @staticmethod
    def delete(session: Session, session_id_int: int):
        with session.begin():
            keycloak_session = cast(Optional[KeycloakSession], session.get(KeycloakSession, session_id_int))
            if not keycloak_session:
                return False
            session.delete(keycloak_session)
        return True

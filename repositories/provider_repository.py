from sqlalchemy.orm import Session
from models import Provider
from typing import cast, Optional


class ProviderRepository:

    @staticmethod
    def create(session: Session, provider: Provider):
        with session.begin():
            session.add(provider)
            session.flush()
            session.refresh(provider)
        return provider

    @staticmethod
    def get_by_id(session: Session, provider_id: int):
        provider = cast(Optional[Provider], session.get(Provider, provider_id))
        return provider

    @staticmethod
    def get_all(session: Session):
        return session.query(Provider).all()

    @staticmethod
    def get_by_code(session: Session, provider_code: str):
        return session.query(Provider).filter(Provider.provider_code == provider_code).all()

    @staticmethod
    def get_active(session: Session):
        return session.query(Provider).filter(Provider.is_active == True).all()

    @staticmethod
    def update(session: Session, provider_id: int, **kwargs):
        with session.begin():
            provider = cast(Optional[Provider], session.get(Provider, provider_id))
            if not provider:
                return None
            for key, value in kwargs.items():
                if hasattr(provider, key):
                    setattr(provider, key, value)
            session.flush()
            session.refresh(provider)
        return provider

    @staticmethod
    def delete(session: Session, provider_id: int):
        with session.begin():
            provider = cast(Optional[Provider], session.get(Provider, provider_id))
            if not provider:
                return False
            session.delete(provider)
        return True

from sqlalchemy.orm import Session
from models import Client
from typing import cast, Optional


class ClientRepository:

    @staticmethod
    def create(session: Session, client: Client):
        with session.begin():
            session.add(client)
            session.flush()
            session.refresh(client)
        return client

    @staticmethod
    def get_by_id(session: Session, client_id: int):
        client = cast(Optional[Client], session.get(Client, client_id))
        return client

    @staticmethod
    def get_all(session: Session):
        return session.query(Client).all()

    @staticmethod
    def get_by_email(session: Session, email: str):
        return session.query(Client).filter(Client.email == email).all()

    @staticmethod
    def get_by_status(session: Session, status: str):
        return session.query(Client).filter(Client.client_status == status).all()

    @staticmethod
    def update(session: Session, client_id: int, **kwargs):
        with session.begin():
            client = cast(Optional[Client], session.get(Client, client_id))
            if not client:
                return None
            for key, value in kwargs.items():
                if hasattr(client, key):
                    setattr(client, key, value)
            session.flush()
            session.refresh(client)
        return client

    @staticmethod
    def delete(session: Session, client_id: int):
        with session.begin():
            client = cast(Optional[Client], session.get(Client, client_id))
            if not client:
                return False
            session.delete(client)
        return True

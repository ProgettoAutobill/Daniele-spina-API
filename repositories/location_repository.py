from sqlalchemy.orm import Session
from models import Location
from typing import cast, Optional


class LocationRepository:

    @staticmethod
    def create(session: Session, location: Location):
        with session.begin():
            session.add(location)
            session.flush()
            session.refresh(location)
        return location

    @staticmethod
    def get_by_id(session: Session, location_id: int):
        location = cast(Optional[Location], session.get(Location, location_id))
        return location

    @staticmethod
    def get_all(session: Session):
        return session.query(Location).all()

    @staticmethod
    def get_by_code(session: Session, location_code: str):
        return session.query(Location).filter(Location.location_code == location_code).all()

    @staticmethod
    def get_active(session: Session):
        return session.query(Location).filter(Location.is_active == True).all()

    @staticmethod
    def update(session: Session, location_id: int, **kwargs):
        with session.begin():
            location = cast(Optional[Location], session.get(Location, location_id))
            if not location:
                return None
            for key, value in kwargs.items():
                if hasattr(location, key):
                    setattr(location, key, value)
            session.flush()
            session.refresh(location)
        return location

    @staticmethod
    def delete(session: Session, location_id: int):
        with session.begin():
            location = cast(Optional[Location], session.get(Location, location_id))
            if not location:
                return False
            session.delete(location)
        return True

from sqlalchemy.orm import Session
from models import CounterDepartment
from typing import cast, Optional


class CounterDepartmentRepository:

    @staticmethod
    def create(session: Session, counter_department: CounterDepartment):
        with session.begin():
            session.add(counter_department)
            session.flush()
            session.refresh(counter_department)
        return counter_department

    @staticmethod
    def get_by_id(session: Session, counter_id: int):
        counter_department = cast(Optional[CounterDepartment], session.get(CounterDepartment, counter_id))
        return counter_department

    @staticmethod
    def get_all(session: Session):
        return session.query(CounterDepartment).all()

    @staticmethod
    def get_by_code(session: Session, counter_code: str):
        return session.query(CounterDepartment).filter(CounterDepartment.counter_code == counter_code).all()

    @staticmethod
    def get_active(session: Session):
        return session.query(CounterDepartment).filter(CounterDepartment.is_active == True).all()

    @staticmethod
    def update(session: Session, counter_id: int, **kwargs):
        with session.begin():
            counter_department = cast(Optional[CounterDepartment], session.get(CounterDepartment, counter_id))
            if not counter_department:
                return None
            for key, value in kwargs.items():
                if hasattr(counter_department, key):
                    setattr(counter_department, key, value)
            session.flush()
            session.refresh(counter_department)
        return counter_department

    @staticmethod
    def delete(session: Session, counter_id: int):
        with session.begin():
            counter_department = cast(Optional[CounterDepartment], session.get(CounterDepartment, counter_id))
            if not counter_department:
                return False
            session.delete(counter_department)
        return True

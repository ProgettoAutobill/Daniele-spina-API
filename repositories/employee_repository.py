from sqlalchemy.orm import Session
from models import Employee
from typing import cast, Optional


class EmployeeRepository:

    @staticmethod
    def create(session: Session, employee: Employee):
        with session.begin():
            session.add(employee)
            session.flush()
            session.refresh(employee)
        return employee

    @staticmethod
    def get_by_id(session: Session, employee_id: int):
        employee = cast(Optional[Employee], session.get(Employee, employee_id))
        return employee

    @staticmethod
    def get_all(session: Session):
        return session.query(Employee).all()

    @staticmethod
    def get_by_email(session: Session, email: str):
        return session.query(Employee).filter(Employee.email == email).all()

    @staticmethod
    def get_active(session: Session):
        return session.query(Employee).filter(Employee.is_active == True).all()

    @staticmethod
    def update(session: Session, employee_id: int, **kwargs):
        with session.begin():
            employee = cast(Optional[Employee], session.get(Employee, employee_id))
            if not employee:
                return None
            for key, value in kwargs.items():
                if hasattr(employee, key):
                    setattr(employee, key, value)
            session.flush()
            session.refresh(employee)
        return employee

    @staticmethod
    def delete(session: Session, employee_id: int):
        with session.begin():
            employee = cast(Optional[Employee], session.get(Employee, employee_id))
            if not employee:
                return False
            session.delete(employee)
        return True

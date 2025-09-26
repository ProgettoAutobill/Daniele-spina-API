from sqlalchemy.orm import Session
from models import SupermarketDepartment
from typing import cast, Optional


class SupermarketDepartmentRepository:

    @staticmethod
    def create(session: Session, department: SupermarketDepartment):
        with session.begin():
            session.add(department)
            session.flush()
            session.refresh(department)
        return department

    @staticmethod
    def get_by_id(session: Session, department_id: int):
        department = cast(Optional[SupermarketDepartment], session.get(SupermarketDepartment, department_id))
        return department

    @staticmethod
    def get_all(session: Session):
        return session.query(SupermarketDepartment).all()

    @staticmethod
    def get_by_code(session: Session, department_code: str):
        return session.query(SupermarketDepartment).filter(
            SupermarketDepartment.department_code == department_code
        ).all()

    @staticmethod
    def update(session: Session, department_id: int, **kwargs):
        with session.begin():
            department = cast(Optional[SupermarketDepartment], session.get(SupermarketDepartment, department_id))
            if not department:
                return None
            for key, value in kwargs.items():
                if hasattr(department, key):
                    setattr(department, key, value)
            session.flush()
            session.refresh(department)
        return department

    @staticmethod
    def delete(session: Session, department_id: int):
        with session.begin():
            department = cast(Optional[SupermarketDepartment], session.get(SupermarketDepartment, department_id))
            if not department:
                return False
            session.delete(department)
        return True

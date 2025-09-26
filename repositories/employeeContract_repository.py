from sqlalchemy.orm import Session
from models import EmployeeContract
from typing import cast, Optional


class EmployeeContractRepository:

    @staticmethod
    def create(session: Session, employee_contract: EmployeeContract):
        with session.begin():
            session.add(employee_contract)
            session.flush()
            session.refresh(employee_contract)
        return employee_contract

    @staticmethod
    def get_by_id(session: Session, contract_id: int):
        employee_contract = cast(Optional[EmployeeContract], session.get(EmployeeContract, contract_id))
        return employee_contract

    @staticmethod
    def get_all(session: Session):
        return session.query(EmployeeContract).all()

    @staticmethod
    def get_by_employee(session: Session, employee_id: int):
        return session.query(EmployeeContract).filter(EmployeeContract.employee_id == employee_id).all()

    @staticmethod
    def get_active(session: Session):
        return session.query(EmployeeContract).filter(EmployeeContract.is_active == True).all()

    @staticmethod
    def update(session: Session, contract_id: int, **kwargs):
        with session.begin():
            employee_contract = cast(Optional[EmployeeContract], session.get(EmployeeContract, contract_id))
            if not employee_contract:
                return None
            for key, value in kwargs.items():
                if hasattr(employee_contract, key):
                    setattr(employee_contract, key, value)
            session.flush()
            session.refresh(employee_contract)
        return employee_contract

    @staticmethod
    def delete(session: Session, contract_id: int):
        with session.begin():
            employee_contract = cast(Optional[EmployeeContract], session.get(EmployeeContract, contract_id))
            if not employee_contract:
                return False
            session.delete(employee_contract)
        return True

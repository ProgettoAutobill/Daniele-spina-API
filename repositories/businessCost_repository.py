from typing import List, Optional, cast
from sqlalchemy.orm import Session
from models import BusinessCost


class BusinessCostRepository:

    @staticmethod
    def create(session: Session, business_cost: BusinessCost) -> BusinessCost:
        with session.begin():
            session.add(business_cost)
            session.flush()
            session.refresh(business_cost)
        return business_cost

    @staticmethod
    def get_by_id(session: Session, cost_id: int) -> Optional[BusinessCost]:
        business_cost = cast(Optional[BusinessCost], session.get(BusinessCost, cost_id))
        return business_cost

    @staticmethod
    def get_all(session: Session):
        return session.query(BusinessCost).all()

    @staticmethod
    def get_by_category(session: Session, category_id: int):
        return session.query(BusinessCost).filter(BusinessCost.category_id == category_id).all()

    @staticmethod
    def get_by_status(session: Session, status: str):
        return session.query(BusinessCost).filter(BusinessCost.payment_status == status).all()

    @staticmethod
    def update(session: Session, cost_id: int, **kwargs) -> Optional[BusinessCost]:
        with session.begin():
            business_cost = cast(Optional[BusinessCost], session.get(BusinessCost, cost_id))
            if not business_cost:
                return None
            for key, value in kwargs.items():
                if hasattr(business_cost, key):
                    setattr(business_cost, key, value)
            session.flush()
            session.refresh(business_cost)
        return business_cost

    @staticmethod
    def delete(session: Session, cost_id: int) -> bool:
        with session.begin():
            business_cost = cast(Optional[BusinessCost], session.get(BusinessCost, cost_id))
            if not business_cost:
                return False
            session.delete(business_cost)
        return True

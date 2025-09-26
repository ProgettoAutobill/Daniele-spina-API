from sqlalchemy.orm import Session
from models import BusinessRevenue
from typing import cast, Optional


class BusinessRevenueRepository:

    @staticmethod
    def create(session: Session, business_revenue: BusinessRevenue):
        with session.begin():
            session.add(business_revenue)
            session.flush()
            session.refresh(business_revenue)
        return business_revenue

    @staticmethod
    def get_by_id(session: Session, revenue_id: int):
        business_revenue = cast(Optional[BusinessRevenue], session.get(BusinessRevenue, revenue_id))
        return business_revenue

    @staticmethod
    def get_all(session: Session):
        return session.query(BusinessRevenue).all()

    @staticmethod
    def get_by_category(session: Session, category_id: int):
        return session.query(BusinessRevenue).filter(BusinessRevenue.category_id == category_id).all()

    @staticmethod
    def get_by_status(session: Session, status: str):
        return session.query(BusinessRevenue).filter(BusinessRevenue.payment_status == status).all()

    @staticmethod
    def update(session: Session, revenue_id: int, **kwargs):
        with session.begin():
            business_revenue = cast(Optional[BusinessRevenue], session.get(BusinessRevenue, revenue_id))
            if not business_revenue:
                return None
            for key, value in kwargs.items():
                if hasattr(business_revenue, key):
                    setattr(business_revenue, key, value)
            session.flush()
            session.refresh(business_revenue)
        return business_revenue

    @staticmethod
    def delete(session: Session, revenue_id: int):
        with session.begin():
            business_revenue = cast(Optional[BusinessRevenue], session.get(BusinessRevenue, revenue_id))
            if not business_revenue:
                return False
            session.delete(business_revenue)
        return True

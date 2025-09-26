from sqlalchemy.orm import Session
from models import FinancialCategory
from typing import cast, Optional


class FinancialCategoryRepository:

    @staticmethod
    def create(session: Session, financial_category: FinancialCategory):
        with session.begin():
            session.add(financial_category)
            session.flush()
            session.refresh(financial_category)
        return financial_category

    @staticmethod
    def get_by_id(session: Session, category_id: int):
        financial_category = cast(Optional[FinancialCategory], session.get(FinancialCategory, category_id))
        return financial_category

    @staticmethod
    def get_all(session: Session):
        return session.query(FinancialCategory).all()

    @staticmethod
    def get_by_code(session: Session, category_code: str):
        return session.query(FinancialCategory).filter(FinancialCategory.category_code == category_code).all()

    @staticmethod
    def get_by_scope(session: Session, scope: str):
        return session.query(FinancialCategory).filter(FinancialCategory.category_scope == scope).all()

    @staticmethod
    def update(session: Session, category_id: int, **kwargs):
        with session.begin():
            financial_category = cast(Optional[FinancialCategory], session.get(FinancialCategory, category_id))
            if not financial_category:
                return None
            for key, value in kwargs.items():
                if hasattr(financial_category, key):
                    setattr(financial_category, key, value)
            session.flush()
            session.refresh(financial_category)
        return financial_category

    @staticmethod
    def delete(session: Session, category_id: int):
        with session.begin():
            financial_category = cast(Optional[FinancialCategory], session.get(FinancialCategory, category_id))
            if not financial_category:
                return False
            session.delete(financial_category)
        return True

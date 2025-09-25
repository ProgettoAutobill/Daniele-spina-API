from datetime import datetime

from sqlalchemy import Integer, String, DateTime, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class FinancialCategory(Base):
    __tablename__ = "financial_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    category_name: Mapped[str] = mapped_column(String(100), nullable=False)
    category_scope: Mapped[str] = mapped_column(String(10), nullable=False)  # cost, revenue, both
    category_type: Mapped[str] = mapped_column(String(15), nullable=False)
    periodicity: Mapped[str] = mapped_column(String(15), default=None)
    category_description: Mapped[str] = mapped_column(String(255), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    business_costs: Mapped[list["BusinessCost"]] = relationship("BusinessCost", back_populates="category")
    business_revenues: Mapped[list["BusinessRevenue"]] = relationship("BusinessRevenue", back_populates="category")


Index("idx_financial_categories_code", FinancialCategory.category_code)
Index("idx_financial_categories_scope", FinancialCategory.category_scope)
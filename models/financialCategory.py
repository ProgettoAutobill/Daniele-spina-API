from sqlalchemy import Integer, String, DateTime, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class FinancialCategory(Base):
    __tablename__ = "financial_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    category_name: Mapped[str] = mapped_column(String(100), nullable=False)
    category_scope: Mapped[str] = mapped_column(String(10), nullable=False)
    category_type: Mapped[str] = mapped_column(String(15), nullable=False)
    periodicity: Mapped[str] = mapped_column(String(15), nullable=True)
    category_description: Mapped[str] = mapped_column(String(255), default="")
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    __table_args__ = (
        CheckConstraint("category_scope IN ('cost','revenue','both')", name="category_scope_check"),
        CheckConstraint(
            "periodicity IS NULL OR periodicity IN ('daily','weekly','monthly','quarterly','semi-annual','yearly')",
            name="periodicity_check"
        ),
    )

    def __repr__(self) -> str:
        return f"<FinancialCategory(code='{self.category_code}', name='{self.category_name}')>"


Index("idx_financial_categories_code", FinancialCategory.category_code)
Index("idx_financial_categories_scope", FinancialCategory.category_scope)

from datetime import datetime

from sqlalchemy import Integer, String, DECIMAL, Date, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class BusinessCost(Base):
    __tablename__ = "business_costs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cost_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("financial_categories.id"), nullable=False)
    cost_description: Mapped[str] = mapped_column(String(255), nullable=False)
    cost_date: Mapped[Date] = mapped_column(Date, nullable=False)
    due_date: Mapped[Date] = mapped_column(Date, default=None)
    supplier_id: Mapped[int] = mapped_column(Integer, ForeignKey("providers.id"), default=None)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey("employees.id"), default=None)
    invoice_number: Mapped[str] = mapped_column(String(50), default=None)
    taxable_amount: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), nullable=False)
    vat_rate: Mapped[DECIMAL] = mapped_column(DECIMAL(5,2), default=0.00)
    vat_amount: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    total_amount: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), nullable=False)
    payment_status: Mapped[str] = mapped_column(String(10), default="pending")
    payment_date: Mapped[Date] = mapped_column(Date, default=None)
    notes: Mapped[str] = mapped_column(String(500), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    category: Mapped["FinancialCategory"] = relationship("FinancialCategory", back_populates="business_costs")
    supplier: Mapped["Provider"] = relationship("Provider")
    employee: Mapped["Employee"] = relationship("Employee")


Index("idx_business_costs_category", BusinessCost.category_id)
Index("idx_business_costs_date", BusinessCost.cost_date)
Index("idx_business_costs_status", BusinessCost.payment_status)
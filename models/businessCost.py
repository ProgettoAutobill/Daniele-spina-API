from sqlalchemy import Integer, String, DECIMAL, Date, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class BusinessCost(Base):
    __tablename__ = "business_costs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cost_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("financial_categories.id"), nullable=False)
    cost_description: Mapped[str] = mapped_column(String(255), nullable=False)
    cost_date: Mapped[Date] = mapped_column(Date, nullable=False)
    due_date: Mapped[Date] = mapped_column(Date, nullable=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("providers.id"), nullable=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=True)
    invoice_number: Mapped[str] = mapped_column(String(50), nullable=True)
    taxable_amount: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), nullable=False)
    vat_rate: Mapped[DECIMAL] = mapped_column(DECIMAL(5,2), default=0.00)
    vat_amount: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    total_amount: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), nullable=False)
    payment_status: Mapped[str] = mapped_column(String(10), default="pending")
    payment_date: Mapped[Date] = mapped_column(Date, nullable=True)
    notes: Mapped[str] = mapped_column(String(500), default="")
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    # Relationships
    category: Mapped["FinancialCategory"] = relationship("FinancialCategory")
    supplier: Mapped["Provider"] = relationship("Provider")
    employee: Mapped["Employee"] = relationship("Employee")

    __table_args__ = (
        CheckConstraint("vat_rate >= 0 AND vat_rate <= 100", name="vat_rate_check"),
        CheckConstraint("supplier_id IS NULL OR employee_id IS NULL", name="supplier_employee_exclusive"),
        CheckConstraint("total_amount = taxable_amount + vat_amount", name="total_equals_taxable_plus_vat"),
        CheckConstraint("payment_status IN ('pending','paid','overdue')", name="payment_status_check"),
    )

    def __repr__(self) -> str:
        return f"<BusinessCost(number='{self.cost_number}', total={self.total_amount})>"


Index("idx_business_costs_category", BusinessCost.category_id)
Index("idx_business_costs_date", BusinessCost.cost_date)
Index("idx_business_costs_status", BusinessCost.payment_status)

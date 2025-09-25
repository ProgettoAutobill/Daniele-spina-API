from sqlalchemy import Integer, String, DECIMAL, Date, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class BusinessRevenue(Base):
    __tablename__ = "business_revenues"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    revenue_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("financial_categories.id"), nullable=False)
    revenue_description: Mapped[str] = mapped_column(String(255), nullable=False)
    revenue_date: Mapped[Date] = mapped_column(Date, nullable=False)
    due_date: Mapped[Date] = mapped_column(Date, nullable=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=True)
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
    category: Mapped["FinancialCategory"] = relationship("FinancialCategory")
    client: Mapped["Client"] = relationship("Client")
    employee: Mapped["Employee"] = relationship("Employee")

    __table_args__ = (
        CheckConstraint("vat_rate >= 0 AND vat_rate <= 100", name="vat_rate_check"),
        CheckConstraint("client_id IS NULL OR employee_id IS NULL", name="client_employee_exclusive"),
        CheckConstraint("total_amount = taxable_amount + vat_amount", name="total_equals_taxable_plus_vat"),
        CheckConstraint("payment_status IN ('pending','received','overdue')", name="payment_status_check"),
    )

    def __repr__(self) -> str:
        return f"<BusinessRevenue(number='{self.revenue_number}', total={self.total_amount})>"


Index("idx_business_revenues_category", BusinessRevenue.category_id)
Index("idx_business_revenues_date", BusinessRevenue.revenue_date)
Index("idx_business_revenues_status", BusinessRevenue.payment_status)

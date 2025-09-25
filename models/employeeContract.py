from datetime import datetime

from sqlalchemy import Integer, String, DECIMAL, Date, Boolean, DateTime, ForeignKey, CheckConstraint, func, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class EmployeeContract(Base):
    __tablename__ = "employee_contracts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), unique=True, nullable=False)
    contract_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    contract_type: Mapped[str] = mapped_column(String(20), nullable=False)
    contract_start_date: Mapped[Date] = mapped_column(Date, nullable=False)
    contract_end_date: Mapped[Date] = mapped_column(Date, default=None)
    job_title: Mapped[str] = mapped_column(String(100), default=None)
    weekly_hours: Mapped[int] = mapped_column(Integer, default=40)
    hourly_rate: Mapped[DECIMAL] = mapped_column(DECIMAL(8,2), default=None)
    monthly_salary: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=None)
    annual_salary: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=None)
    trial_period_days: Mapped[int] = mapped_column(Integer, default=90)
    notice_period_days: Mapped[int] = mapped_column(Integer, default=30)
    vacation_days_per_year: Mapped[int] = mapped_column(Integer, default=20)
    sick_leave_days_per_year: Mapped[int] = mapped_column(Integer, default=10)
    contract_level: Mapped[str] = mapped_column(String(100), default=None)
    ccnl_type: Mapped[str] = mapped_column(String(50), default=None)
    benefits: Mapped[str] = mapped_column(String(1000), default="")
    notes: Mapped[str] = mapped_column(String(1000), default="")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    contract_signed_date: Mapped[Date] = mapped_column(Date, default=None)
    contract_renewed_date: Mapped[Date] = mapped_column(Date, default=None)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="contract")


Index("idx_employee_contracts_employee_id", EmployeeContract.employee_id)
Index("idx_employee_contracts_number", EmployeeContract.contract_number)
Index("idx_contracts_type_active", EmployeeContract.contract_type, EmployeeContract.is_active)
from sqlalchemy import Integer, String, DECIMAL, Date, Boolean, DateTime, ForeignKey, CheckConstraint, func, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class EmployeeContract(Base):
    __tablename__ = "employee_contracts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), unique=True, nullable=False)
    contract_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    contract_type: Mapped[str] = mapped_column(String(20), nullable=False)
    contract_start_date: Mapped[Date] = mapped_column(Date, nullable=False)
    contract_end_date: Mapped[Date] = mapped_column(Date, nullable=True)
    job_title: Mapped[str] = mapped_column(String(100), nullable=True)
    weekly_hours: Mapped[int] = mapped_column(Integer, default=40)
    hourly_rate: Mapped[DECIMAL] = mapped_column(DECIMAL(8,2), nullable=True)
    monthly_salary: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), nullable=True)
    annual_salary: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), nullable=True)
    trial_period_days: Mapped[int] = mapped_column(Integer, default=90)
    notice_period_days: Mapped[int] = mapped_column(Integer, default=30)
    benefits: Mapped[str] = mapped_column(String(1000), default="")
    notes: Mapped[str] = mapped_column(String(1000), default="")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    contract_signed_date: Mapped[Date] = mapped_column(Date, nullable=True)
    contract_renewed_date: Mapped[Date] = mapped_column(Date, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    employee: Mapped["Employee"] = relationship("Employee", back_populates="contract")

    def __repr__(self) -> str:
        return f"<EmployeeContract(number='{self.contract_number}')>"


Index("idx_employee_contracts_employee_id", EmployeeContract.employee_id)
Index("idx_employee_contracts_number", EmployeeContract.contract_number)
Index("idx_contracts_type_active", EmployeeContract.contract_type, EmployeeContract.is_active)

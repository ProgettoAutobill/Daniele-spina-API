from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DECIMAL, Date, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    employee_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    personal_email: Mapped[str] = mapped_column(String(100), default=None)
    phone: Mapped[str] = mapped_column(String(20), default=None)
    personal_phone: Mapped[str] = mapped_column(String(20), default=None)
    hire_date: Mapped[Date] = mapped_column(Date, nullable=False)
    location_id: Mapped[int] = mapped_column(Integer, ForeignKey("locations.id"), default=None)
    salary: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=None)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    location: Mapped["Location"] = relationship("Location", back_populates="employees")
    contract: Mapped["EmployeeContract"] = relationship(
        "EmployeeContract", back_populates="employee", cascade="all, delete-orphan", uselist=False
    )


Index("idx_employees_code", Employee.employee_code)
Index("idx_employees_email", Employee.email)
Index("idx_employees_location", Employee.location_id)

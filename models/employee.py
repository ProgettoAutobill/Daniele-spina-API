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
    personal_email: Mapped[str] = mapped_column(String(100), nullable=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    personal_phone: Mapped[str] = mapped_column(String(20), nullable=True)
    hire_date: Mapped[Date] = mapped_column(Date, nullable=False)
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"), nullable=True)
    salary: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    location: Mapped["Location"] = relationship("Location", back_populates="employees")
    contract: Mapped["EmployeeContract"] = relationship("EmployeeContract", back_populates="employee", uselist=False, cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint(
            "email GLOB '*@*.*' AND length(email) >=5 AND length(email) <=100 AND "
            "email NOT GLOB '*@*@*' AND email NOT GLOB '.*@*' AND email NOT GLOB '*@.*'",
            name="email_format_check"
        ),
        CheckConstraint(
            "personal_email IS NULL OR (personal_email GLOB '*@*.*' AND length(personal_email) >=5 AND length(personal_email) <=100 AND "
            "personal_email NOT GLOB '*@*@*' AND personal_email NOT GLOB '.*@*' AND personal_email NOT GLOB '*@.*')",
            name="personal_email_format_check"
        ),
        CheckConstraint(
            "phone IS NULL OR (length(phone) >=8 AND length(phone) <=20 AND phone GLOB '+*[0-9]*')",
            name="phone_format_check"
        ),
        CheckConstraint(
            "personal_phone IS NULL OR (length(personal_phone) >=8 AND length(personal_phone) <=20 AND personal_phone GLOB '+*[0-9]*')",
            name="personal_phone_format_check"
        ),
    )

    def __repr__(self) -> str:
        return f"<Employee(code='{self.employee_code}', name='{self.first_name} {self.last_name}')>"


Index("idx_employees_code", Employee.employee_code)
Index("idx_employees_email", Employee.email)
Index("idx_employees_location", Employee.location_id)

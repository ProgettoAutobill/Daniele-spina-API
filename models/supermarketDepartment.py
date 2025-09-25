from datetime import datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class SupermarketDepartment(Base):
    __tablename__ = "supermarket_departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    department_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    department_name: Mapped[str] = mapped_column(String(100), nullable=False)
    department_type: Mapped[str] = mapped_column(String(20), default="standard")
    parent_department_id: Mapped[int] = mapped_column(Integer, ForeignKey("supermarket_departments.id"), default=None)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    sub_departments: Mapped[list["SupermarketDepartment"]] = relationship(
        "SupermarketDepartment", backref="parent_department", remote_side=[id]
    )
    products: Mapped[list["Product"]] = relationship("Product", back_populates="department")

Index("idx_supermarket_departments_code", SupermarketDepartment.department_code)
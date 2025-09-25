from sqlalchemy import Integer, String, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class SupermarketDepartment(Base):
    __tablename__ = "supermarket_departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    department_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    department_name: Mapped[str] = mapped_column(String(100), nullable=False)
    department_type: Mapped[str] = mapped_column(String(20), default="standard")
    parent_department_id: Mapped[int] = mapped_column(ForeignKey("supermarket_departments.id"), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    parent_department: Mapped["SupermarketDepartment"] = relationship("SupermarketDepartment", remote_side=[id])
    products: Mapped[list["Product"]] = relationship("Product", back_populates="department")

    __table_args__ = (
        CheckConstraint(
            "department_type IN ('frozen','fresh','dry','beverages','cleaning','personal_care','standard')",
            name="department_type_check"
        ),
    )

    def __repr__(self) -> str:
        return f"<SupermarketDepartment(code='{self.department_code}', name='{self.department_name}')>"


Index("idx_supermarket_departments_code", SupermarketDepartment.department_code)

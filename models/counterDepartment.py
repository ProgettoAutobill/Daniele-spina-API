from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class CounterDepartment(Base):
    __tablename__ = "counter_departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    counter_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    counter_name_en: Mapped[str] = mapped_column(String(100), nullable=False)
    counter_name_it: Mapped[str] = mapped_column(String(100), nullable=False)
    counter_description: Mapped[str] = mapped_column(String(255), default=None)
    is_weighable: Mapped[bool] = mapped_column(Boolean, default=False)
    requires_refrigeration: Mapped[bool] = mapped_column(Boolean, default=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    products: Mapped[list["Product"]] = relationship("Product", back_populates="counter")


Index("idx_counter_departments_code", CounterDepartment.counter_code)
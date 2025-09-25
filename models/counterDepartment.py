from sqlalchemy import Integer, String, Boolean, DateTime, Index, func
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class CounterDepartment(Base):
    __tablename__ = "counter_departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    counter_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    counter_name_en: Mapped[str] = mapped_column(String(100), nullable=False)
    counter_name_it: Mapped[str] = mapped_column(String(100), nullable=False)
    counter_description: Mapped[str] = mapped_column(String(255), nullable=True)
    is_weighable: Mapped[bool] = mapped_column(Boolean, default=False)
    requires_refrigeration: Mapped[bool] = mapped_column(Boolean, default=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    def __repr__(self) -> str:
        return f"<CounterDepartment(code='{self.counter_code}', name='{self.counter_name_en}')>"


Index("idx_counter_departments_code", CounterDepartment.counter_code)

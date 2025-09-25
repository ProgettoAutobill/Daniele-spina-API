from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime, DECIMAL, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    movement_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    movement_type: Mapped[str] = mapped_column(String(20), nullable=False)
    movement_direction: Mapped[str] = mapped_column(String(3), nullable=False)
    provider_id: Mapped[int] = mapped_column(Integer, ForeignKey("providers.id"), default=None)
    loyalty_card_id: Mapped[int] = mapped_column(Integer, ForeignKey("loyalty_cards.id"), default=None)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey("employees.id"), nullable=False)
    movement_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    due_date: Mapped[datetime] = mapped_column(DateTime, default=None)
    delivery_date: Mapped[datetime] = mapped_column(DateTime, default=None)
    movement_status: Mapped[str] = mapped_column(String(20), default="completed")
    payment_method: Mapped[str] = mapped_column(String(20), default=None)
    cash_received: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=None)
    change_given: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    subtotal: Mapped[DECIMAL] = mapped_column(DECIMAL(12,2), default=None)
    discount_total: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    tax_total: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    final_total: Mapped[DECIMAL] = mapped_column(DECIMAL(12,2), default=None)
    payment_terms: Mapped[str] = mapped_column(String(255), default=None)
    notes: Mapped[str] = mapped_column(String(1000), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    employee: Mapped["Employee"] = relationship("Employee")
    provider: Mapped["Provider"] = relationship("Provider")
    loyalty_card: Mapped["LoyaltyCard"] = relationship("LoyaltyCard")
    items: Mapped[list["StockMovementItem"]] = relationship(
        "StockMovementItem", back_populates="stock_movement", cascade="all, delete-orphan"
    )


Index("idx_stock_movements_number", StockMovement.movement_number)
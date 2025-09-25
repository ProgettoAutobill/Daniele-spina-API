from datetime import datetime

from sqlalchemy import Integer, DECIMAL, String, Date, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class StockMovementItem(Base):
    __tablename__ = "stock_movement_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    stock_movement_id: Mapped[int] = mapped_column(Integer, ForeignKey("stock_movements.id", ondelete="CASCADE"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    quantity_ordered: Mapped[DECIMAL] = mapped_column(DECIMAL(10,3), default=None)
    quantity_actual: Mapped[DECIMAL] = mapped_column(DECIMAL(10,3), nullable=False)
    unit_cost: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=None)
    unit_price: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=None)
    discount_amount: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    discount_percent: Mapped[DECIMAL] = mapped_column(DECIMAL(5,2), default=0.00)
    line_subtotal: Mapped[DECIMAL] = mapped_column(DECIMAL(12,2), default=None)
    line_total: Mapped[DECIMAL] = mapped_column(DECIMAL(12,2), default=None)
    tax_rate: Mapped[DECIMAL] = mapped_column(DECIMAL(5,2), default=0.00)
    batch_number: Mapped[str] = mapped_column(String(50), default=None)
    items_expiry_date: Mapped[Date] = mapped_column(Date, default=None)
    line_notes: Mapped[str] = mapped_column(String(500), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    stock_movement: Mapped["StockMovement"] = relationship("StockMovement", back_populates="items")
    product: Mapped["Product"] = relationship("Product")


Index("idx_stock_movement_items_unique", StockMovementItem.stock_movement_id, StockMovementItem.product_id, unique=True)
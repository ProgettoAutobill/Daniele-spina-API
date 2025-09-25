from sqlalchemy import Integer, DECIMAL, String, Date, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class StockMovementItem(Base):
    __tablename__ = "stock_movement_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    stock_movement_id: Mapped[int] = mapped_column(ForeignKey("stock_movements.id", ondelete="CASCADE"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity_ordered: Mapped[DECIMAL] = mapped_column(DECIMAL(10,3), nullable=True)
    quantity_actual: Mapped[DECIMAL] = mapped_column(DECIMAL(10,3), nullable=False)
    unit_cost: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), nullable=True)
    unit_price: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), nullable=True)
    discount_amount: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    discount_percent: Mapped[DECIMAL] = mapped_column(DECIMAL(5,2), default=0.00)
    line_subtotal: Mapped[DECIMAL] = mapped_column(DECIMAL(12,2), nullable=True)
    line_total: Mapped[DECIMAL] = mapped_column(DECIMAL(12,2), nullable=True)
    tax_rate: Mapped[DECIMAL] = mapped_column(DECIMAL(5,2), default=0.00)
    batch_number: Mapped[str] = mapped_column(String(50), nullable=True)
    items_expiry_date: Mapped[Date] = mapped_column(Date, nullable=True)
    line_notes: Mapped[str] = mapped_column(String(500), default="")
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    stock_movement: Mapped["StockMovement"] = relationship("StockMovement", back_populates="items")
    product: Mapped["Product"] = relationship("Product")

    __table_args__ = (
        CheckConstraint("quantity_actual >= 0", name="quantity_actual_check"),
        CheckConstraint("discount_amount >= 0 AND discount_percent >= 0", name="discount_check"),
        # Unique constraint equivalent to SQL UNIQUE(stock_movement_id, product_id)
        Index("uix_stock_movement_item_movement_product", "stock_movement_id", "product_id", unique=True),
    )

    def __repr__(self) -> str:
        return f"<StockMovementItem(movement_id={self.stock_movement_id}, product_id={self.product_id})>"

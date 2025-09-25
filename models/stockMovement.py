from sqlalchemy import Integer, String, Boolean, DateTime, DECIMAL, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    movement_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    movement_type: Mapped[str] = mapped_column(String(20), nullable=False)
    movement_direction: Mapped[str] = mapped_column(String(3), nullable=False)
    provider_id: Mapped[int] = mapped_column(ForeignKey("providers.id"), nullable=True)
    loyalty_card_id: Mapped[int] = mapped_column(ForeignKey("loyalty_cards.id"), nullable=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)
    movement_date: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())
    due_date: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    delivery_date: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    movement_status: Mapped[str] = mapped_column(String(20), default="completed")
    payment_method: Mapped[str] = mapped_column(String(20), nullable=True)
    cash_received: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), nullable=True)
    change_given: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    subtotal: Mapped[DECIMAL] = mapped_column(DECIMAL(12,2), nullable=True)
    discount_total: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    tax_total: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    final_total: Mapped[DECIMAL] = mapped_column(DECIMAL(12,2), nullable=True)
    payment_terms: Mapped[str] = mapped_column(String(255), nullable=True)
    notes: Mapped[str] = mapped_column(String(1000), default="")
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    provider: Mapped["Provider"] = relationship("Provider")
    loyalty_card: Mapped["LoyaltyCard"] = relationship("LoyaltyCard")
    employee: Mapped["Employee"] = relationship("Employee")
    items: Mapped[list["StockMovementItem"]] = relationship("StockMovementItem", back_populates="stock_movement", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint(
            "movement_type IN ('purchase','sale','adjustment','transfer','loss','return')",
            name="movement_type_check"
        ),
        CheckConstraint(
            "movement_direction IN ('IN','OUT')",
            name="movement_direction_check"
        ),
        CheckConstraint(
            "(movement_type = 'sale' AND loyalty_card_id IS NOT NULL) OR (movement_type != 'sale')",
            name="sale_loyalty_card_check"
        ),
        CheckConstraint(
            "(movement_type = 'purchase' AND provider_id IS NOT NULL) OR (movement_type != 'purchase')",
            name="purchase_provider_check"
        ),
        CheckConstraint(
            "(movement_type = 'sale' AND payment_method IS NOT NULL) OR (movement_type != 'sale')",
            name="sale_payment_method_check"
        ),
        CheckConstraint(
            "movement_status IN ('pending','completed','verified','paid','disputed','cancelled')",
            name="movement_status_check"
        ),
        CheckConstraint(
            "payment_method IS NULL OR payment_method IN ('bank_transfer','cash','card','mixed','check','credit','voucher_payment','other')",
            name="payment_method_check"
        ),
    )

    def __repr__(self) -> str:
        return f"<StockMovement(number='{self.movement_number}', type='{self.movement_type}')>"


Index("idx_stock_movements_number", StockMovement.movement_number)
Index("idx_stock_movements_employee", StockMovement.employee_id)
Index("idx_stock_movements_provider", StockMovement.provider_id)

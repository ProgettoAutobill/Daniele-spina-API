from sqlalchemy import Integer, String, Boolean, DateTime, DECIMAL, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class LoyaltyCard(Base):
    __tablename__ = "loyalty_cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id", ondelete="CASCADE"), unique=True, nullable=False)
    card_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    card_status: Mapped[str] = mapped_column(String(20), default="active")
    points: Mapped[int] = mapped_column(Integer, default=0)
    points_earned: Mapped[int] = mapped_column(Integer, default=0)
    points_used: Mapped[int] = mapped_column(Integer, default=0)
    points_expires_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    card_tier: Mapped[str] = mapped_column(String(20), default="bronze")
    issue_date: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())
    card_expiry_date: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    last_used_date: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    total_transactions: Mapped[int] = mapped_column(Integer, default=0)
    total_spent: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    client: Mapped["Client"] = relationship("Client", back_populates="loyalty_card")

    __table_args__ = (
        CheckConstraint(
            "card_status IN ('active','inactive','blocked','expired')",
            name="card_status_check"
        ),
        CheckConstraint("points >= 0 AND points_earned >= 0 AND points_used >= 0", name="points_check"),
        CheckConstraint("card_tier IN ('bronze','silver','gold','platinum')", name="card_tier_check"),
    )

    def __repr__(self) -> str:
        return f"<LoyaltyCard(number='{self.card_number}', client_id={self.client_id})>"


Index("idx_loyalty_cards_number", LoyaltyCard.card_number)
Index("idx_loyalty_cards_client", LoyaltyCard.client_id)

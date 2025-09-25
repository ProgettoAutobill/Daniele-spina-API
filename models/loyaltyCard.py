from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime, DECIMAL, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class LoyaltyCard(Base):
    __tablename__ = "loyalty_cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), unique=True, nullable=False)
    card_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    card_status: Mapped[str] = mapped_column(String(20), default="active")
    points: Mapped[int] = mapped_column(Integer, default=0)
    points_earned: Mapped[int] = mapped_column(Integer, default=0)
    points_used: Mapped[int] = mapped_column(Integer, default=0)
    points_expires_at: Mapped[datetime] = mapped_column(DateTime, default=None)
    card_tier: Mapped[str] = mapped_column(String(20), default="bronze")
    issue_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    card_expiry_date: Mapped[datetime] = mapped_column(DateTime, default=None)
    last_used_date: Mapped[datetime] = mapped_column(DateTime, default=None)
    total_transactions: Mapped[int] = mapped_column(Integer, default=0)
    total_spent: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    client: Mapped["Client"] = relationship("Client", back_populates="loyalty_card")


Index("idx_loyalty_cards_number", LoyaltyCard.card_number)
Index("idx_loyalty_cards_client", LoyaltyCard.client_id)
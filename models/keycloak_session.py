from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime, CheckConstraint, Index, Time, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class KeycloakSession(Base):
    __tablename__ = "keycloak_sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    session_id: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    access_token_hash: Mapped[str] = mapped_column(String(128), default="")
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    ip_address: Mapped[str] = mapped_column(String(45), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship("User", back_populates="sessions")


Index("idx_sessions_user_id", KeycloakSession.user_id)
Index("idx_sessions_session_id", KeycloakSession.session_id)
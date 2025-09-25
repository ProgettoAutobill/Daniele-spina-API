from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class AuthToken(Base):
    __tablename__ = "auth_tokens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    token_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    token_type: Mapped[str] = mapped_column(String(10), nullable=False, default="access")
    expires_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    is_revoked: Mapped[bool] = mapped_column(Boolean, default=False)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=True)
    client_info: Mapped[str] = mapped_column(String(500), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    user: Mapped["User"] = relationship("User", back_populates="auth_tokens")

    __table_args__ = (
        CheckConstraint("token_type IN ('access', 'refresh', 'reset')", name="token_type_check"),
        CheckConstraint(
            "ip_address IS NULL OR "
            "(ip_address GLOB '*.*.*.*' AND length(ip_address) >= 7 AND length(ip_address) <= 15) OR "
            "(ip_address GLOB '*:*' AND length(ip_address) >= 3 AND length(ip_address) <= 39)",
            name="ip_address_format_check"
        ),
    )

    def __repr__(self) -> str:
        return f"<AuthToken(user_id={self.user_id}, type='{self.token_type}', revoked={self.is_revoked})>"


Index("idx_auth_tokens_user_id", AuthToken.user_id)
Index("idx_auth_tokens_hash", AuthToken.token_hash)

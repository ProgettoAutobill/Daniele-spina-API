from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class AuthLog(Base):
    __tablename__ = "auth_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    username: Mapped[str] = mapped_column(String(50), nullable=True)
    action_performed: Mapped[str] = mapped_column(String(30), nullable=False)
    success: Mapped[bool] = mapped_column(Boolean, nullable=False)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=True)
    user_agent: Mapped[str] = mapped_column(String(500), nullable=True)
    details: Mapped[str] = mapped_column(String(1000), default="")
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    user: Mapped["User"] = relationship("User", back_populates="auth_logs")

    __table_args__ = (
        CheckConstraint(
            "action_performed IN ('login', 'logout', 'failed_login', 'token_refresh', "
            "'password_reset', 'account_locked', 'account_unlocked')",
            name="action_performed_check"
        ),
        CheckConstraint(
            "ip_address IS NULL OR "
            "(ip_address GLOB '*.*.*.*' AND length(ip_address) >= 7 AND length(ip_address) <= 15) OR "
            "(ip_address GLOB '*:*' AND length(ip_address) >= 3 AND length(ip_address) <= 39)",
            name="ip_address_format_check"
        ),
    )

    def __repr__(self) -> str:
        return f"<AuthLog(user_id={self.user_id}, action='{self.action_performed}', success={self.success})>"


Index("idx_auth_logs_user_id", AuthLog.user_id)
Index("idx_auth_logs_created", AuthLog.created_at)

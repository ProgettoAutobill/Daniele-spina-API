from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    password_salt: Mapped[str] = mapped_column(String(64), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    role: Mapped["Role"] = relationship("Role", back_populates="users")
    auth_tokens: Mapped[list["AuthToken"]] = relationship("AuthToken", back_populates="user", cascade="all, delete-orphan")
    auth_logs: Mapped[list["AuthLog"]] = relationship("AuthLog", back_populates="user")

    __table_args__ = (
        CheckConstraint(
            "email GLOB '*@*.*' AND "
            "length(email) >= 5 AND length(email) <= 100 AND "
            "email NOT GLOB '*@*@*' AND "
            "email NOT GLOB '.*@*' AND "
            "email NOT GLOB '*@.*'",
            name="email_format_check"
        ),
        CheckConstraint(
            "length(password_hash) >= 32 AND length(password_hash) <= 128 AND "
            "password_hash GLOB '[0-9a-fA-F]*'",
            name="password_hash_check"
        ),
        CheckConstraint(
            "length(password_salt) >= 16 AND length(password_salt) <= 64 AND "
            "password_salt GLOB '[0-9a-fA-F]*'",
            name="password_salt_check"
        ),
    )

    def __repr__(self) -> str:
        return f"<User(username='{self.username}', email='{self.email}', is_active={self.is_active})>"


Index("idx_users_username", User.username)
Index("idx_users_email", User.email)
Index("idx_users_role_id", User.role_id)

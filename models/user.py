from datetime import datetime
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    keycloak_user_id: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), default="")
    last_name: Mapped[str] = mapped_column(String(100), default="")
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"), nullable=False, default=4)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    role: Mapped["Role"] = relationship("Role", back_populates="users")
    sessions: Mapped[list["KeycloakSession"]] = relationship(
        "KeycloakSession", back_populates="user", cascade="all, delete-orphan"
    )


Index("idx_users_keycloak_id", User.keycloak_user_id)
Index("idx_users_username", User.username)
Index("idx_users_role_id", User.role_id)

from sqlalchemy import Integer, String, CheckConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class UserPermission(Base):
    __tablename__ = "user_permissions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    permission_name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    permission_description: Mapped[str] = mapped_column(String(255), default="")
    required_role_level: Mapped[int] = mapped_column(Integer, default=0)


Index("idx_user_permissions_name", UserPermission.permission_name)
Index("idx_user_permissions_level", UserPermission.required_role_level)
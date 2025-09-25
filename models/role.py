from sqlalchemy import Integer, String, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    role_description: Mapped[str] = mapped_column(String(255), default="")
    role_level: Mapped[int] = mapped_column(Integer, default=0)
    users: Mapped[list["User"]] = relationship("User", back_populates="role")


Index("idx_roles_level", Role.role_level)

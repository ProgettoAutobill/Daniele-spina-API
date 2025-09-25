from sqlalchemy import Integer, String, Index
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class AuthorizedScript(Base):
    __tablename__ = "authorized_scripts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    script_name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    script_path: Mapped[str] = mapped_column(String(500), nullable=False)
    script_hash: Mapped[str] = mapped_column(String(128), nullable=True)
    script_description: Mapped[str] = mapped_column(String(255), default="")
    required_role_level: Mapped[int] = mapped_column(Integer, default=0)

    def __repr__(self) -> str:
        return f"<AuthorizedScript(name='{self.script_name}', path='{self.script_path}', required_level={self.required_role_level})>"

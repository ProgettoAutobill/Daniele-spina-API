from sqlalchemy import Integer, String, Boolean, DateTime, CheckConstraint, Index, Time, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Location(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    location_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    location_name: Mapped[str] = mapped_column(String(100), nullable=False)
    location_type: Mapped[str] = mapped_column(String(30), nullable=False, default="store")
    location_address: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    postal_code: Mapped[str] = mapped_column(String(10), nullable=True)
    country_code: Mapped[str] = mapped_column(String(3), nullable=False)
    region_state: Mapped[str] = mapped_column(String(100), nullable=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    email: Mapped[str] = mapped_column(String(254), nullable=True)
    opening_time: Mapped[str] = mapped_column(Time, default="08:00:00")
    closing_time: Mapped[str] = mapped_column(Time, default="20:00:00")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    notes: Mapped[str] = mapped_column(String(500), default="")
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    employees: Mapped[list["Employee"]] = relationship("Employee", back_populates="location")

    __table_args__ = (
        CheckConstraint(
            "location_type IN ('store','warehouse','office','headquarters','distribution_center')",
            name="location_type_check"
        ),
        CheckConstraint(
            "phone IS NULL OR (length(phone) >= 8 AND length(phone) <= 20 AND phone GLOB '+*[0-9]*')",
            name="phone_format_check"
        ),
        CheckConstraint(
            "email IS NULL OR (email GLOB '*@*.*' AND length(email) >= 5 AND length(email) <= 254 AND "
            "email NOT GLOB '*@*@*' AND email NOT GLOB '.*@*' AND email NOT GLOB '*@.*')",
            name="email_format_check"
        ),
    )

    def __repr__(self) -> str:
        return f"<Location(code='{self.location_code}', name='{self.location_name}')>"


Index("idx_locations_code", Location.location_code)
Index("idx_locations_active_type", Location.is_active, Location.location_type)

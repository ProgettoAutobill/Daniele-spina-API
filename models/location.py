from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime, CheckConstraint, Index, Time, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Location(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    location_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    location_name: Mapped[str] = mapped_column(String(100), nullable=False)
    location_type: Mapped[str] = mapped_column(
        String(30), nullable=False, default="store"
    )
    location_address: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    postal_code: Mapped[str] = mapped_column(String(10), default=None)
    country_code: Mapped[str] = mapped_column(String(3), nullable=False)
    region_state: Mapped[str] = mapped_column(String(100), default=None)
    phone: Mapped[str] = mapped_column(String(20), default=None)
    email: Mapped[str] = mapped_column(String(254), default=None)
    opening_time: Mapped[Time] = mapped_column(Time, default="08:00:00")
    closing_time: Mapped[Time] = mapped_column(Time, default="20:00:00")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    notes: Mapped[str] = mapped_column(String(500), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    employees: Mapped[list["Employee"]] = relationship("Employee", back_populates="location")


Index("idx_locations_code", Location.location_code)
Index("idx_locations_active_type", Location.is_active, Location.location_type)
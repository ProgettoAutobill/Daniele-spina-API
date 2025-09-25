from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime, DECIMAL, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Provider(Base):
    __tablename__ = "providers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    provider_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    provider_name: Mapped[str] = mapped_column(String(100), nullable=False)
    provider_type: Mapped[str] = mapped_column(String(20), default="supplier")
    contact_person: Mapped[str] = mapped_column(String(100), default=None)
    contact_info: Mapped[str] = mapped_column(String(255), default=None)
    email: Mapped[str] = mapped_column(String(100), default=None)
    phone: Mapped[str] = mapped_column(String(20), default=None)
    provider_address: Mapped[str] = mapped_column(String(255), default=None)
    city: Mapped[str] = mapped_column(String(100), default=None)
    postal_code: Mapped[str] = mapped_column(String(10), default=None)
    country: Mapped[str] = mapped_column(String(50), default="Italy")
    vat_number: Mapped[str] = mapped_column(String(20), default=None)
    tax_code: Mapped[str] = mapped_column(String(20), default=None)
    website: Mapped[str] = mapped_column(String(255), default=None)
    payment_terms_days: Mapped[int] = mapped_column(Integer, default=30)
    discount_percentage: Mapped[DECIMAL] = mapped_column(DECIMAL(5,2), default=0.00)
    notes: Mapped[str] = mapped_column(String(1000), default="")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    products: Mapped[list["Product"]] = relationship("Product", back_populates="supplier")

Index("idx_providers_code", Provider.provider_code)
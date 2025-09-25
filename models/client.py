from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime, Date, DECIMAL, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    client_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), default=None)
    phone: Mapped[str] = mapped_column(String(20), default=None)
    client_address: Mapped[str] = mapped_column(String(255), default=None)
    city: Mapped[str] = mapped_column(String(100), default=None)
    postal_code: Mapped[str] = mapped_column(String(10), default=None)
    country: Mapped[str] = mapped_column(String(50), default="Italy")
    birth_date: Mapped[Date] = mapped_column(Date, default=None)
    gender: Mapped[str] = mapped_column(String(10), default=None)
    tax_code: Mapped[str] = mapped_column(String(20), default=None)
    vat_number: Mapped[str] = mapped_column(String(20), default=None)
    client_category: Mapped[str] = mapped_column(String(20), default="standard")
    client_status: Mapped[str] = mapped_column(String(20), default="active")
    marketing_consent: Mapped[bool] = mapped_column(Boolean, default=False)
    newsletter_consent: Mapped[bool] = mapped_column(Boolean, default=False)
    sms_consent: Mapped[bool] = mapped_column(Boolean, default=False)
    privacy_consent: Mapped[bool] = mapped_column(Boolean, default=True)
    consent_date: Mapped[datetime] = mapped_column(DateTime, default=None)
    registration_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    last_visit_date: Mapped[datetime] = mapped_column(DateTime, default=None)
    last_purchase_date: Mapped[datetime] = mapped_column(DateTime, default=None)
    total_purchases: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    visit_count: Mapped[int] = mapped_column(Integer, default=0)
    notes: Mapped[str] = mapped_column(String(2000), default=None)
    registered_by: Mapped[int] = mapped_column(Integer, ForeignKey("employees.id"), default=None)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    registered_employee: Mapped["Employee"] = relationship("Employee")
    loyalty_card: Mapped["LoyaltyCard"] = relationship("LoyaltyCard", back_populates="client", uselist=False)

Index("idx_clients_code", Client.client_code)
Index("idx_clients_email", Client.email)
Index("idx_clients_category_status", Client.client_category, Client.client_status)
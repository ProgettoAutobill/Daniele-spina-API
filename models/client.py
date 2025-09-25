from sqlalchemy import Integer, String, Boolean, DateTime, Date, DECIMAL, ForeignKey, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    client_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    client_address: Mapped[str] = mapped_column(String(255), nullable=True)
    city: Mapped[str] = mapped_column(String(100), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(10), nullable=True)
    country: Mapped[str] = mapped_column(String(50), default="Italy")
    birth_date: Mapped[Date] = mapped_column(Date, nullable=True)
    gender: Mapped[str] = mapped_column(String(10), nullable=True)
    tax_code: Mapped[str] = mapped_column(String(20), nullable=True)
    vat_number: Mapped[str] = mapped_column(String(20), nullable=True)
    client_category: Mapped[str] = mapped_column(String(20), default="standard")
    client_status: Mapped[str] = mapped_column(String(20), default="active")
    marketing_consent: Mapped[bool] = mapped_column(Boolean, default=False)
    newsletter_consent: Mapped[bool] = mapped_column(Boolean, default=False)
    sms_consent: Mapped[bool] = mapped_column(Boolean, default=False)
    privacy_consent: Mapped[bool] = mapped_column(Boolean, default=True)
    consent_date: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    registration_date: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())
    last_visit_date: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    last_purchase_date: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    total_purchases: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=0.00)
    visit_count: Mapped[int] = mapped_column(Integer, default=0)
    notes: Mapped[str] = mapped_column(String(2000), nullable=True)
    registered_by: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    registered_employee: Mapped["Employee"] = relationship("Employee")
    loyalty_card: Mapped["LoyaltyCard"] = relationship("LoyaltyCard", back_populates="client", uselist=False, cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint(
            "email IS NULL OR (email GLOB '*@*.*' AND length(email) >= 5 AND length(email) <= 100 AND "
            "email NOT GLOB '*@*@*' AND email NOT GLOB '.*@*' AND email NOT GLOB '*@.*')",
            name="email_format_check"
        ),
        CheckConstraint(
            "phone IS NULL OR (length(phone) >= 8 AND length(phone) <= 20 AND "
            "(phone GLOB '+[0-9]*' OR phone GLOB '[0-9]*') AND phone NOT GLOB '*[a-zA-Z]*')",
            name="phone_format_check"
        ),
        CheckConstraint(
            "gender IS NULL OR gender IN ('M','F','Other')",
            name="gender_check"
        ),
        CheckConstraint(
            "client_category IN ('standard','premium','vip','business')",
            name="client_category_check"
        ),
        CheckConstraint(
            "client_status IN ('active','inactive','suspended','blocked')",
            name="client_status_check"
        ),
    )

    def __repr__(self) -> str:
        return f"<Client(code='{self.client_code}', name='{self.first_name} {self.last_name}')>"


Index("idx_clients_code", Client.client_code)
Index("idx_clients_email", Client.email)
Index("idx_clients_category_status", Client.client_category, Client.client_status)

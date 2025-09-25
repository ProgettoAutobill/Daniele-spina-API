from sqlalchemy import Integer, String, Boolean, DateTime, DECIMAL, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Provider(Base):
    __tablename__ = "providers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    provider_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    provider_name: Mapped[str] = mapped_column(String(100), nullable=False)
    provider_type: Mapped[str] = mapped_column(String(20), default="supplier")
    contact_person: Mapped[str] = mapped_column(String(100), nullable=True)
    contact_info: Mapped[str] = mapped_column(String(255), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    provider_address: Mapped[str] = mapped_column(String(255), nullable=True)
    city: Mapped[str] = mapped_column(String(100), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(10), nullable=True)
    country: Mapped[str] = mapped_column(String(50), default="Italy")
    vat_number: Mapped[str] = mapped_column(String(20), nullable=True)
    tax_code: Mapped[str] = mapped_column(String(20), nullable=True)
    website: Mapped[str] = mapped_column(String(255), nullable=True)
    payment_terms_days: Mapped[int] = mapped_column(Integer, default=30)
    discount_percentage: Mapped[DECIMAL] = mapped_column(DECIMAL(5,2), default=0.00)
    notes: Mapped[str] = mapped_column(String(1000), default="")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    products: Mapped[list["Product"]] = relationship("Product", back_populates="supplier")

    __table_args__ = (
        CheckConstraint(
            "provider_type IN ('supplier','delivery')",
            name="provider_type_check"
        ),
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
    )

    def __repr__(self) -> str:
        return f"<Provider(code='{self.provider_code}', name='{self.provider_name}')>"


Index("idx_providers_code", Provider.provider_code)

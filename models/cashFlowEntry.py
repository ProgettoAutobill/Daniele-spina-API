from models.base import Base
from sqlalchemy import Column, DateTime, Float, String


class CashFlowEntry(Base):
    """
    Base class for all cash flow entries.
    Table: cash_flow_entry

    Columns:
        id (String, PK): Unique identifier for the cash flow entry.
        amount (Float): Transaction amount (positive for inflow, negative for outflow).
        currency (String): ISO currency code (e.g., EUR, USD, GBP, CHF, etc.).
        created_at (DateTime): Timestamp when the entry was created (UTC).
        updated_at (DateTime): Timestamp when the entry was last updated (UTC, NULL if never updated).
        description (String): Short description or reason for the entry.
        note (String): Additional notes, comments, or details for the entry.
        cashflow_type (String): Type of cash flow entry (for polymorphic mapping, e.g., operative_expense, revenue, etc.).
    """
    __tablename__ = 'cash_flow_entry'
    __mapper_args__ = {
        'polymorphic_identity': 'cash_flow_entry',
        'polymorphic_on': 'cashflow_type'
    }
    id = Column(
        String(64),
        primary_key = True,
        doc = "Unique identifier for the cash flow entry. UUID recommended."
    )
    amount = Column(
        Float,
        nullable = False,
        doc = "Transaction amount (positive for inflow, negative for outflow)."
    )
    currency = Column(
        String(3),
        nullable = False,
        default = 'EUR',
        doc = "ISO currency code (e.g., EUR, USD, GBP, CHF, etc.)"
    )
    created_at = Column(
        DateTime,
        nullable = False,
        doc = "Timestamp when the entry was created (UTC)."
    )
    updated_at = Column(
        DateTime,
        nullable = True,
        doc = "Timestamp when the entry was last updated (UTC, NULL if never updated)."
    )
    description = Column(
        String(256),
        nullable = True,
        doc = "Short description or reason for the entry."
    )
    note = Column(
        String(512),
        nullable = True,
        doc = "Additional notes, comments, or details for the entry."
    )
    cashflow_type = Column(
        String(50),
        nullable = False,
        doc = "Type of cash flow entry (for polymorphic mapping, e.g., operative_expense, revenue, etc.)"
    )

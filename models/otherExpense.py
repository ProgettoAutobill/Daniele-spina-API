from sqlalchemy import Column, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from models.expense import Expense


class OtherExpense(Expense):
    """
    OtherExpense: Other operative costs (transport, logistics, miscellaneous, etc.)
    Table: other_expense
    Inherits: expense

    Columns:
        provider_id (String, FK): Reference to the provider contract (FK to provider)
        contract_type (String): Type of contract/service (transport, logistics, courier, etc.)
        contract_tax_amount (Float): Total tax/fiscal amount as specified in the supply contract
        departure_date (DateTime): Departure date for transport or logistics service
        arrival_date (DateTime): Arrival date for transport or logistics service
    Relationships:
        provider (relationship): Reference to the provider associated with this expense (FK to provider)
    """
    __tablename__ = 'other_expense'
    __mapper_args__ = {
        'polymorphic_identity': 'other_expense',
    }
    id = Column(
        String(64),
        ForeignKey('expense.id'),
        primary_key = True,
        doc="Primary key for other expense (FK to expense)"
    )
    provider_id = Column(
        String(64),
        ForeignKey(
            'provider.id',
            ondelete = 'SET NULL'
        ),
        nullable = False,
        doc = "Reference to the provider contract (FK to provider: contract for transport, logistics, miscellaneous, etc.)"
    )
    service_type = Column(
        String(64),
        nullable = True,
        doc = "Type of contract/service (e.g., transport, logistics, courier, etc.)"
    )
    contract_tax_amount = Column(
        Float,
        nullable = True,
        doc = "Total tax/fiscal amount as specified in the supply contract (importo fiscale contrattuale, non aliquota)"
    )
    # --- transport logistics specific attributes ---
    departure_date = Column(
        DateTime,
        nullable = True,
        doc = "Departure date for transport or logistics service (if applicable)"
    )
    arrival_date = Column(
        DateTime,
        nullable = True,
        doc = "Arrival date for transport or logistics service (if applicable)"
    )
    provider = relationship(
        'Provider',
        back_populates = 'other_expenses',
        foreign_keys = ['OtherExpense.provider_id'],
        doc = "Reference to the provider associated with this expense"
    )
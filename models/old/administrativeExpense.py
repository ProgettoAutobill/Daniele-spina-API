from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.expense import Expense


class AdministrativeExpense(Expense):
    """
    AdministrativeExpense: Administrative costs (accountant, software, banking, insurance, etc.)
    Table: administrative_expense
    Inherits: expense

    Columns:
        administrative_provider_id (String, FK): Reference to the administrative provider (FK to provider)
        administrative_type (String): Type of administrative expense (accounting, software, banking, insurance, etc.)
        contract_tax_amount (Float): Total tax/fiscal amount as specified in the administrative contract
    Relationships:
        administrative_provider (relationship): Reference to the administrative provider associated with this expense (FK to provider)
    """
    __tablename__ = 'administrative_expense'
    __mapper_args__ = {
        'polymorphic_identity': 'administrative_expense',
    }
    id = Column(
        String(64),
        ForeignKey('expense.id'),
        primary_key = True,
        doc = "Primary key for administrative expense (FK to expense)"
    )
    administrative_provider_id = Column(
        String(128),
        ForeignKey(
            'provider.id',
            ondelete = 'SET NULL'
        ),
        nullable = False,
        doc = "Reference to the administrative provider (FK to provider)"
    )
    administrative_type = Column(
        String(64),
        nullable = True,
        doc = "Type of administrative expense (e.g., accounting, software, banking, insurance, etc.)"
    )
    contract_tax_amount = Column(
        Float,
        nullable = True,
        doc = "Total tax/fiscal amount as specified in the facility contract"
    )
    administrative_provider = relationship(
        'Provider',
        back_populates = 'administrative_expenses',
        foreign_keys = ["AdministrativeExpense.administrative_provider_id"],
        doc = "Reference to the administrative provider associated with this expense"
    )
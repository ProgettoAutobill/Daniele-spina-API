from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.expense import Expense


class UtilityExpense(Expense):
    """
    UtilityExpense: Utility bills and related costs (electricity, gas, water, internet, etc.)
    Table: utility_expense
    Inherits: expense

    Columns:
        utility_provider_id (String, FK): Reference to the utility provider (FK to provider)
        utility_type (String): Type of utility (e.g., electricity, gas, water, internet, etc.)
        vat_amount (Float): VAT amount for this bill/entry
        excise_amount (Float): Excise duty amount for this bill/entry
        other_tax_amount (Float): Other taxes or fiscal charges for this bill/entry
    Relationships:
        utility_provider (relationship): Reference to the utility provider associated with this expense (FK to provider)
    """
    __tablename__ = 'utility_expense'
    __mapper_args__ = {
        'polymorphic_identity': 'utility_expense',
    }
    id = Column(
        String(64),
        ForeignKey('expense.id'),
        primary_key = True,
        doc = "Primary key for utility expense (FK to expense)"
    )
    utility_provider_id = Column(
        String(128),
        ForeignKey(
            'provider.id',
            ondelete = 'SET NULL'
        ),
        nullable = False,
        doc = "Reference to the utility provider (FK to provider)"
    )
    utility_type = Column(
        String(32),
        nullable = False,
        doc = "Type of utility (e.g., electricity, gas, water, internet, etc.)"
    )
    vat_amount = Column(
        Float,
        nullable = True,
        doc = "VAT (IVA) amount for this bill/entry (importo IVA in bolletta/voce)"
    )
    excise_amount = Column(
        Float,
        nullable = True,
        doc = "Excise duty (accisa) amount for this bill/entry (importo accisa in bolletta/voce)"
    )
    other_tax_amount = Column(
        Float,
        nullable = True,
        doc = "Other taxes or fiscal charges for this bill/entry (altre imposte e tasse in bolletta)"
    )
    utility_provider = relationship(
        'Provider',
        back_populates = 'utility_expenses',
        foreign_keys = ['UtilityExpense.utility_provider_id'],
        doc = "Reference to the utility provider associated with this expense"
    )
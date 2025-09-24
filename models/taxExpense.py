from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from models.expense import Expense


class TaxExpense(Expense):
    """
    Tax expenses: VAT, local taxes, IRAP, and other fiscal obligations.
    Table: tax_expense
    Inherits: expense

    Columns:
        id (String, PK, FK): Unique identifier for the tax expense (FK to expense)
        model_tax_id (String, FK): Reference to the tax model (FK to tax_model)
        state_entity_id (String, FK): Reference to the state entity (e.g., government, municipality, etc.)
        tax_base (Float): Taxable base amount for this tax expense (imponibile)
    Relationships:
        model_tax (relationship): Reference to the tax model associated with this expense (FK to tax_model)
        state_entity (relationship): Reference to the state entity associated with this tax expense (FK to state_entity)
    """
    __tablename__ = 'tax_expense'
    __mapper_args__ = {
        'polymorphic_identity': 'tax_expense',
    }
    id = Column(
        String(64),
        ForeignKey('expense.id'),
        primary_key=True,
        doc="Primary key for tax expense (FK to expense)"
    )
    model_tax_id = Column(
        String(64),
        ForeignKey('tax_model.id'),
        nullable = False,
        doc = "Reference to the tax model (FK to tax_model)"
    )
    state_entity_id = Column(
        String(64),
        ForeignKey('state_entity.id'),
        nullable = True,
        doc = "Reference to the state entity (e.g., government, municipality, etc.)"
    )
    tax_base = Column(
        Float,
        nullable = True,
        doc = "Taxable base amount for this tax expense (imponibile)"
    )
    model_tax = relationship(
        'TaxModel',
        back_populates = 'tax_expenses',
        foreign_keys = ['TaxExpense.model_tax_id'],
        doc = "Reference to the tax model associated with this expense"
    )
    state_entity = relationship(
        'StateEntity',
        back_populates = 'tax_expenses',
        foreign_keys = ['TaxExpense.state_entity_id'],
        doc = "Reference to the state entity associated with this tax expense"
    )
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.expense import Expense


class FinanceExpense(Expense):
    """
    FinanceExpense: Financial expenses such as interests, commissions, banking costs, loans, equity, etc.
    Table: finance_expense
    Inherits: expense

    Columns:
        id (String, PK, FK): Unique identifier for the finance expense (FK to expense)
        finance_id (String, FK): Reference to the finance type (FK to finance)
    Relationships:
        finance (relationship): Reference to the finance type associated with this expense (FK to finance)
        stakeholder (relationship): Reference to the stakeholder associated with this expense (FK to stakeholder)
    """
    __tablename__ = 'finance_expense'
    __mapper_args__ = {
        'polymorphic_identity': 'finance_expense',
    }
    id = Column(
        String(64),
        ForeignKey('expense.id'),
        primary_key = True,
        doc = "Primary key for finance expense (FK to expense)"
    )
    finance_id = Column(
        String(64),
        ForeignKey('finance.id'),
        nullable = True,
        doc = "Reference to the finance type (FK to finance)"
    )
    finance = relationship(
        'Finance',
        back_populates = 'finance_expenses',
        foreign_keys = ['FinanceExpense.finance_id'],
        doc = "Reference to the finance type associated with this expense"
    )


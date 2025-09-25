from sqlalchemy import Column, DateTime, Float, ForeignKey, String

from models.old.cashFlowEntry import CashFlowEntry


class Expense(CashFlowEntry):
    """
    Base abstract Table for operative expenses (not related to product/material transactions).
    Examples: staff salaries, rent, utilities, marketing, maintenance, administrative costs,
    logistics, licenses, consumables, etc.
    Table: expense
    Inherits: cash_flow_entry

    Columns:
        id (String, PK, FK): Unique identifier for the expense (FK to cash_flow_entry).
        payment_due_date (DateTime): Due date for payment (mandatory).
        payment_date (DateTime): Actual payment date (if null, payment has not been accounted/registered)
        period_start (DateTime): Start date of the period (if recurring expense)
        period_end (DateTime): End date of the period (if recurring expense)
        penalty_amount (Float): Penalty amount for late payment or contract violations (if applicable).
        interest (Float): Interest amount for late payments (if applicable).
    """
    __tablename__ = 'expense'
    __mapper_args__ = {
        'polymorphic_identity': 'expense',
    }
    id = Column(
        String(64),
        ForeignKey('cash_flow_entry.id'),
        primary_key = True,
        doc = "Unique identifier for the operative expense (FK to cash_flow_entry)"
    )
    payment_due_date = Column(
        DateTime,
        nullable = False,
        doc = "Due date for payment (mandatory)"
    )
    payment_date = Column(
        DateTime,
        nullable = True,
        doc = "Actual payment date (if null, payment has not been accounted/registered)"
    )
    period_start = Column(
        DateTime,
        nullable = True,
        doc = "Start date of the period (if applicable, e.g., for recurring expenses)"
    )
    period_end = Column(
        DateTime,
        nullable = True,
        doc = "End date of the period (if applicable, e.g., for recurring expenses)"
    )
    penalty_amount = Column(
        Float,
        nullable = True,
        doc = "Penalty amount for late payment or contract violations (if applicable)"
    )
    interest = Column(
        Float,
        nullable = True,
        doc = "Interest amount for late payments (if applicable)"
    )
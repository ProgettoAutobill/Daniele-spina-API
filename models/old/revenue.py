from sqlalchemy import Column, DateTime, ForeignKey, String

from models.old.cashFlowEntry import CashFlowEntry


class Revenue(CashFlowEntry):
    """
    Base class for operative revenues (investimenti equity, prestiti, finanziamenti, etc.).
    Table: revenue
    Inherits: cash_flow_entry

    Column:
        id (String, PK, FK): Unique identifier for the revenue (FK to cash_flow_entry)
        payment_due_date (DateTime): Due date for payment (mandatory)
        payment_date (DateTime): Actual payment date (if null, payment has not been accounted/registered)
        revenue_type (String): Discriminator for polymorphic mapping (e.g., service revenue, other revenue, etc.)
    Relationships:
        stakeholder (relationship): Reference to the stakeholder associated with this revenue (FK to stakeholder, SET NULL on delete)
        finance (relationship): Reference to the finance type associated with this revenue (FK to finance, SET NULL on delete)
    """
    __tablename__ = 'revenue'
    __mapper_args__ = {
        'polymorphic_identity': 'revenue',
        'polymorphic_on': 'revenue_type'
    }
    id = Column(
        String(64),
        ForeignKey('cash_flow_entry.id'),
        primary_key = True,
        doc = "Unique identifier for the revenue (FK to cash_flow_entry)"
    )
    payment_date = Column(
        DateTime,
        nullable = True,
        doc = "Actual payment date (if null, payment has not been accounted/registered)"
    )
    revenue_type = Column(
        String(32),
        nullable = False,
        doc = "Discriminator for polymorphic mapping"
    )
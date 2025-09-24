from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from models.revenue import Revenue


class OtherRevenue(Revenue):
    """
    Base class for operative revenues.
    Examples: investimenti equity, soldi con prestiti, finanziamenti, etc.
    Table: revenue
    Inherits: cash_flow_entry

    Columns:
        id (String, PK, FK): Unique identifier for the revenue (FK to cash_flow_entry)
        stakeholder_id (String, FK): Reference to the stakeholder or entity related to this financial revenue
        finance_id (String, FK): Reference to the finance type (FK to finance)
        payment_due_date (DateTime): Due date for payment (mandatory)
        payment_date (DateTime): Actual payment date (if null, payment has not been accounted/registered)
    Relationships:
        stakeholder (relationship): Reference to the stakeholder associated with this revenue (FK to stakeholder)
        finance (relationship): Reference to the finance type associated with this revenue (FK to finance)
    """
    __tablename__ = 'operative_revenue'
    __mapper_args__ = {
        'polymorphic_identity': 'operative_revenue',
    }
    id = Column(
        String(64),
        ForeignKey('revenue.id'),
        primary_key = True,
        doc = "Unique identifier for the operative revenue (FK to cash_flow_entry)"
    )
    stakeholder_id = Column(
        String(64),
        ForeignKey('stakeholder.id'),
        nullable = True,
        doc = "Stakeholder or entity related to this financial revenue"
    )
    finance_id = Column(
        String(64),
        ForeignKey('finance.id'),
        nullable = True,
        doc = "Reference to the finance type (FK to finance)"
    )
    payment_due_date = Column(
        DateTime,
        nullable = False,
        doc = "Due date for payment (mandatory)"
    )
    stakeholder = relationship(
        'Stakeholder',
        back_populates = 'revenues',
        foreign_keys = ['Revenue.stakeholder_id'],
        doc = "Reference to the stakeholder associated with this revenue"
    )
    finance = relationship(
        'Finance',
        back_populates = 'revenues',
        foreign_keys = ['Revenue.finance_id'],
        doc = "Reference to the finance type associated with this revenue"
    )
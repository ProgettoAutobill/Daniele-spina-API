from sqlalchemy import Column,  Float, ForeignKey, String
from sqlalchemy.orm import relationship
from models.businessEntity import BusinessEntity


class Stakeholder(BusinessEntity):
    """
    Stakeholder: Entity or individual with an interest in the business.
    Table: stakeholder
    Inherits: business_entity

    Columns:
        id (String, PK, FK): Primary key, foreign key to business_entity.id
        stakeholder_code (String, unique): Internal/external stakeholder code
        stakeholder_type (String): Type of stakeholder (individual, institutional, etc.)
        contact_person (String): Main contact person
        investment_amount (Float): Amount invested (if applicable)
    Relationships:
        finance_expense (relationship): All finance expenses associated with this stakeholder (FK to finance_expense)
        revenue (relationship): All revenue entries associated with this stakeholder (FK to revenue)
    """
    __tablename__ = 'stakeholder'
    __mapper_args__ = {
        'polymorphic_identity': 'stakeholder',
    }
    id = Column(
        String(64),
        ForeignKey('business_entity.id'),
        primary_key=True
    )
    stakeholder_code = Column(
        String(32),
        nullable=True,
        unique=True,
        doc="Internal/external stakeholder code"
    )
    stakeholder_type = Column(
        String(64),
        nullable=True,
        doc="Type of stakeholder (individual, institutional, etc.)"
    )
    contact_person = Column(
        String(128),
        nullable=True,
        doc="Main contact person"
    )
    investment_amount = Column(
        Float,
        nullable=True,
        doc="Amount invested (if applicable)"
    )
    finance_expense = relationship(
        'FinanceExpense',
        back_populates='stakeholder',
        passive_deletes=True,
        doc="All finance expenses associated with this stakeholder (set NULL on stakeholder delete)"
    )
    revenue = relationship(
        'Revenue',
        back_populates='stakeholder',
        passive_deletes=True,
        doc="All revenue entries associated with this stakeholder (set NULL on stakeholder delete)"
    )
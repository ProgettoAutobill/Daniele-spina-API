from database.sessionDB import Base
from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Finance(Base):
    """
    Finance: Stores finance types and models for the organization.
    Table: finance

    Columns:
        id (String, PK): Primary key for the finance model
        name (String): Finance model name
        description (String): Description of the finance model
        is_active (String): If the finance type is active
        entity (String): Entity or organization related to this finance type
        calculation_method (String): Calculation method for this finance type
        reference_law (String): Legal reference or regulation for this finance type
        notes (String): Free notes
    """
    __tablename__ = 'finance'
    id = Column(
        String(64),
        primary_key = True,
        doc = "Primary key for the finance model"
    )
    name = Column(
        String(64),
        nullable = False,
        doc = "Finance model name"
    )
    stakeholder_id = Column(
        String(64),
        ForeignKey(
            'stakeholder.id',
            ondelete = 'SET NULL'
        ),
        nullable = True,
        doc = "FK to stakeholder for finance models related to stakeholders"
    )
    description = Column(
        String(255),
        nullable = True,
        doc = "Description of the finance model"
    )
    is_active = Column(
        Boolean,
        nullable = False,
        default = True
        ,
        doc = "If the finance type is active"
    )
    entity = Column(
        String(64),
        nullable = True,
        doc = "Entity or organization related to this finance type"
    )
    calculation_method = Column(
        String(64),
        nullable = True,
        doc = "Calculation method for this finance type"
    )
    reference_law = Column(
        String(128),
        nullable = True,
        doc = "Legal reference or regulation for this finance type"
    )
    notes = Column(
        String(255),
        nullable = True,
        doc = "Free notes"
    )
    stakeholder = relationship(
        'Stakeholder',
        back_populates = 'finance_expense',
        foreign_keys = ['Finance.stakeholder_id'],
        uselist = False,
        doc = "Reference to the stakeholder related to this finance model (one-to-one)"
    )
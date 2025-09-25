from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.businessEntity import BusinessEntity


class StateEntity(BusinessEntity):
    """
    StateEntity: Government body or public agency.
    Table: state_entity
    Inherits: business_entity

    Columns:
        id (String, PK, FK): Primary key, foreign key to business_entity.id
        office_code (String): Office/department code
        region (String): Region or administrative area
        legal_representative (String): Legal representative
        entity_level (String): Level of state entity (national, regional, municipal)
        public_body_type (String): Type of public body (ministry, agency, municipality)
        tax_office_code (String): Tax office/fiscal code
    Relationships:
        tax_expense (relationship): All tax expenses associated with this state entity (FK to tax_expense)
    """
    __tablename__ = 'state_entity'
    __mapper_args__ = {
        'polymorphic_identity': 'state_entity',
    }
    id = Column(
        String(64),
        ForeignKey('business_entity.id'),
        primary_key = True
    )
    office_code = Column(
        String(32),
        nullable = True,
        doc = "Office/department code"
    )
    region = Column(
        String(64),
        nullable = True,
        doc = "Region or administrative area"
    )
    legal_representative = Column(
        String(128),
        nullable = True,
        doc = "Legal representative"
    )
    entity_level = Column(
        String(32),
        nullable = True,
        doc = "Level of state entity (national, regional, municipal)"
    )
    public_body_type = Column(
        String(64),
        nullable = True,
        doc = "Type of public body (ministry, agency, municipality)"
    )
    tax_office_code = Column(
        String(32),
        nullable = True,
        doc = "Tax office/fiscal code"
    )
    tax_expense = relationship(
        'TaxExpense',
        back_populates = 'state_entity',
        passive_deletes = True,
        doc = "All tax expenses associated with this state entity (set NULL on state entity delete)"
    )
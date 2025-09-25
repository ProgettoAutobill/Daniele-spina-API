from database.sessionDB import Base
from sqlalchemy import Boolean, Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship


class TaxModel(Base):
    """
    Stores tax models and types (VAT, F24, INPS, WITHHOLDING, etc.).
    Table: tax_model

    Attributes:
        id (String, PK): Primary key for the tax model
        name (String): Tax name (e.g. VAT, F24, INPS, WITHHOLDING)
        description (String): Description of the tax type
        periodicity (String): Periodicity (e.g. 'quarterly', 'monthly', 'annual')
        aliquot (Float): Tax rate or aliquot (e.g. 22.0 for VAT, None for F24)
        code (String): Tax code, INPS code, etc.
        is_active (String): If the tax model is active
        calculation_method (String): Calculation method (e.g. 'from_invoices', 'fixed', etc.)
        reference_law (String): Legal reference or regulation
        notes (String): Free notes
    """
    __tablename__ = 'tax_model'
    id = Column(
        String(64),
        primary_key = True,
        doc = "Primary key for the tax model"
    )
    name = Column(
        String(64),
        nullable = False,
        doc = "Tax name (e.g. VAT, F24, INPS, WITHHOLDING)"
    )
    entity_state_id = Column(
        String(64),
        ForeignKey(
            'state_entity.id',
            ondelete = 'SET NULL'
        ),
        nullable = True,
        doc = "FK to state_entity for tax models related to state entities"
    )
    description = Column(
        String(255),
        nullable = True,
        doc = "Description of the tax type"
    )
    periodicity = Column(
        String(32),
        nullable = False,
        doc = "Periodicity (e.g. 'quarterly', 'monthly', 'annual')"
    )
    aliquot = Column(
        Float,
        nullable = True,
        doc = "Tax rate or aliquot (e.g. 22.0 for VAT, None for F24)"
    )
    code = Column(
        String(32),
        nullable = True,
        doc = "Tax code, INPS code, etc."
    )
    is_active = Column(
        Boolean,
        nullable = False,
        default = True,
        doc = "If the tax model is active"
    )
    calculation_method = Column(
        String(64),
        nullable = True,
        doc = "Calculation method (e.g. 'from_invoices', 'fixed', etc.)"
    )
    reference_law = Column(
        String(128),
        nullable = True,
        doc = "Legal reference or regulation"
    )
    notes = Column(
        String(255),
        nullable = True,
        doc = "Free notes"
    )
    entity_state = relationship(
        'StateEntity',
        back_populates = 'tax_models',
        foreign_keys = ['TaxModel.entity_state_id'],
        uselist = False,
        doc = "Reference to the state entity related to this tax model (one-to-one)"
    )

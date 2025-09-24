from models.base import Base
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class CollaboratorContract(Base):
    """
    Stores contracts for collaborators (external, internal, consultants, etc.).
    Table: collaborator_contract

    Columns:
        id (String, PK): Primary key for the contract
        collaborator_id (String, FK): FK to collaborator
        contract_type (String): Type of contract (e.g., freelance, consulting, temporary)
        qualification (String): Professional qualification or level
        fee (Float): Agreed fee or compensation
        start_date (Date): Contract start date
        end_date (Date): Contract end date (if applicable)
        period_of_probe (Integer): Probation period in days (if applicable)
        tax_rate (Float): Tax rate (%) applied to compensation
        notes (String): Additional notes or comments about the contract
        collaborator (relationship): Relationship to Collaborator
    """
    __tablename__ = 'collaborator_contract'
    id = Column(
        String(64),
        primary_key = True
    )
    collaborator_id = Column(
        String(64),
        ForeignKey(
            'collaborator.id',
            ondelete = 'SET NULL'
        ),
        nullable = False,
        doc = "FK to collaborator"
    )
    contract_type = Column(
        String(32),
        nullable = True,
        doc = "Type of contract (e.g., freelance, consulting, temporary)"
    )
    qualification = Column(
        String(64),
        nullable = True,
        doc = "Professional qualification or level"
    )
    fee = Column(
        Float,
        nullable = True,
        doc = "Agreed fee or compensation"
    )
    start_date = Column(
        Date,
        nullable = True,
        doc = "Contract start date"
    )
    end_date = Column(
        Date,
        nullable = True,
        doc = "Contract end date (if applicable)"
    )
    period_of_probe = Column(
        Integer,
        nullable = True,
        doc = "Probation period in days (if applicable)"
    )
    tax_rate = Column(
        Float,
        nullable = True,
        doc = "Tax rate (%) applied to compensation"
    )
    notes = Column(
        String(255),
        nullable = True,
        doc = "Additional notes or comments about the contract"
    )
    collaborator = relationship(
        'Collaborator',
        back_populates = 'collaborations',
        foreign_keys = ['CollaboratorContract.collaborator_id'],
        uselist = False,
        doc = "Relationship to Collaborator (one-to-one)"
    )
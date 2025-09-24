from sqlalchemy import Column, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from models.userBase import UserBase


class Collaborator(UserBase):
    """
    Stores collaborators (external or internal) of the organization.
    Table: collaborator
    Inherits: user

    Columns:
        id (String, PK, FK): Primary key, foreign key to user.id
        collaborator_code (String, unique): Internal collaborator code or reference
        hire_date (Date): Date of hiring
        termination_date (Date): Date of termination (if applicable)
        work_phone (String): Work phone number
        work_email (String): Work email address
        location_id (String, FK): Location assigned to the collaborator (FK to location.id, SET NULL on delete)
        supervisor_id (String, FK): ID of the supervisor/manager (FK to employee.id, SET NULL on delete)
    Relationships:
        collaboration (relationship): Collaboration contract details
        location (relationship): Location assigned to the collaborator (FK to location.id)
        supervisor (relationship): Supervisor/manager of the collaborator (FK to employee.id)
    """
    __tablename__ = 'collaborator'
    __mapper_args__ = {
        'polymorphic_identity': 'collaborator',
    }
    id = Column(
        String(64),
        ForeignKey('user.id'),
        primary_key = True
    )
    collaborator_code = Column(
        String(32),
        nullable = True,
        unique = True,
        doc = "Internal collaborator code or reference"
    )
    hire_date = Column(
        Date,
        nullable = False,
        doc = "Date of hiring"
    )
    termination_date = Column(
        Date,
        nullable = True,
        doc = "Date of termination (if applicable)"
    )
    work_phone = Column(
        String(32),
        nullable = True,
        doc = "Work phone number"
    )
    work_email = Column(
        String(128),
        nullable = True,
        doc = "Work email address"
    )
    location_id = Column(
        String(64),
        ForeignKey(
            'location.id',
            ondelete = 'SET NULL'
        ),
        nullable = True,
        doc = "Location assigned to the employee (FK to location.id, SET NULL on delete)"
    )
    supervisor_id = Column(
        String(64),
        ForeignKey(
            'employee.id',
            ondelete = 'SET NULL'
        ),
        nullable = True,
        doc = "ID of the supervisor/manager (FK to employee.id, SET NULL on delete)"
    )
    role_id = Column(
        String(64),
        ForeignKey(
            'role.id',
            ondelete = 'SET NULL'
        ),
        nullable = True,
        doc = "Role assigned to the user (FK to role.id, SET NULL on delete)"
    )
    collaboration = relationship(
        'CollaborationContract',
        back_populates = 'collaborator',
        passive_deletes = True,
        uselist = False
    )
    location = relationship(
        'Location',
        back_populates = 'collaborators',
        foreign_keys = ['Collaborator.location_id'],
        uselist = False,
        doc = "Reference to the location assigned to the collaborator (one-to-one)"
    )
    supervisor = relationship(
        'Employee',
        back_populates = 'collaborators',
        foreign_keys = ['Collaborator.supervisor_id'],
        uselist = False,
        doc = "Reference to the supervisor/manager of the collaborator (one-to-one)"
    )
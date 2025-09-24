from models.base import Base
from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Authentication(Base):
    """
    Table for employee authentication details.
    Stores login credentials and authentication methods for employees.
    Table: authentication

    Columns:
        id (String): Unique identifier for the authentication record (PK).
        employee_id (String): Reference to the employee (FK to employee.id).
        username (String): Username for login (unique).
        password_hash (String): Hashed password for security.
        two_factor_enabled (Boolean): Indicates if two-factor authentication is enabled.
        permission (String): Permission level or role for authentication (optional).
    Relationships:
        employee (relationship): Relationship to Employee, back_populates 'authentication'.
        access_logs (relationship): Relationship to AccessLog, back_populates 'authentication'.
    """
    __tablename__ = 'authentication'
    id = Column(
        String(64),
        primary_key = True
    )
    employee_id = Column(
        String(64),
        ForeignKey('employee.id'),
        nullable = False,
        doc = "FK to employee"
    )
    username = Column(
        String(64),
        nullable = False,
        unique = True,
        doc = "Username for login"
    )
    password_hash = Column(
        String(128),
        nullable = False,
        doc = "Hashed password for security"
    )
    two_factor_enabled = Column(
        Boolean,
        default = True,
        doc = "Indicates if two-factor authentication is enabled"
    )
    permission = Column(
        String(64),
        nullable = True,
        doc = "Permission level or role for authentication (optional)"
    )
    employee = relationship(
        'Employee',
        back_populates = 'authentication',
        foreign_keys = ['Authentication.employee_id'],
        uselist = False,
        doc = "Reference to the employee associated with this authentication record"
    )
    access_logs = relationship(
        'AccessLog',
        back_populates = 'authentication',
        cascade = 'all, delete-orphan',
        doc = "All access log entries for this authentication record"
    )
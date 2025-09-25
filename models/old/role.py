from database.sessionDB import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Role(Base):
    """
    Stores employee roles or job functions. Each role can be assigned to one or more employees.
    Table: role

    Columns:
        id (String): Unique identifier for the role (PK).
        name (String): Name of the role or job function (unique).
        level (String): Level or seniority of the role (e.g., junior, mid, senior).
        description (String): Description or notes about the role.
    Relationships:
        user (relationship): Relationship to UserBase, back_populates 'role'.
    """
    __tablename__ = 'role'
    id = Column(
        String(64),
        primary_key = True
    )
    name = Column(
        String(64),
        nullable = False,
        unique = True,
        doc = "Name of the role or job function"
    )
    level = Column(
        String(32),
        nullable = True,
        doc = "Level or seniority of the role (e.g., junior, mid, senior)"
    )
    description = Column(
        String(255),
        nullable = True,
        doc = "Description or notes about the role"
    )
    user = relationship(
        'UserBase',
        back_populates = 'role',
        passive_deletes = True,
        doc = "Reference to the user associated with this role"
    )
from models.base import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Location(Base):
    """
    Work location or office. Each location can have multiple employees.
    Table: location

    Columns:
        id (String, PK): Unique identifier for the location
        name (String): Location name
        address (String): Location address
        city (String): City
        province (String): Province/region
        country (String): Country
        zip_code (String): Postal or ZIP code
        notes (String): Notes or description
    Relationships:
        employees (relationship): All employees assigned to this location
        collaborators (relationship): All collaborators assigned to this location
    """
    __tablename__ = 'location'
    id = Column(
        String(64),
        primary_key = True,
        doc = "Primary key for the location"
    )
    name = Column(
        String(128),
        nullable = False,
        doc = "Location name"
    )
    address = Column(
        String(255),
        nullable = True,
        doc = "Location address"
    )
    city = Column(
        String(64),
        nullable = True,
        doc = "City"
    )
    province = Column(
        String(32),
        nullable = True,
        doc = "Province/region"
    )
    country = Column(
        String(64),
        nullable = True,
        doc = "Country"
    )
    zip_code = Column(
        String(16),
        nullable = True,
        doc = "Postal or ZIP code"
    )
    notes = Column(
        String(255),
        nullable = True,
        doc = "Notes or description"
    )
    employees = relationship(
        'Employee',
        back_populates = 'location',
        passive_deletes = True,
        doc = "All employees assigned to this location (set NULL on location delete)"
    )
    collaborators = relationship(
        'Collaborator',
        back_populates = 'location',
        passive_deletes = True,
        doc = "All collaborators assigned to this location (set NULL on location delete)"
    )

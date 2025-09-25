from database.sessionDB import Base
from sqlalchemy import Column, Date, String


class UserBase(Base):
    """
    Table for user-related entities (employee, client, etc.).
    Table: user

    Inherited by:
        - Employee
        - Collaborator
        - Client

    Columns:
        id (String, PK): Unique identifier for the user
        name (String): First name
        surname (String): Surname
        date_of_birth (Date): Date of birth
        place_of_birth (String): Place of birth
        fiscal_code (String, unique): Personal fiscal code
        address (String): Residential address
        city (String): City of residence
        province (String): Province/region of residence
        country (String): Country of residence
        phone (String): Personal phone number
        email (String): Personal email address
        notes (String): Additional notes or comments
        entity_user (String): Discriminator for polymorphic mapping (employee, client, etc.)
    """
    __tablename__ = 'user'
    __mapper_args__ = {
        'polymorphic_on': 'entity_user',
        'polymorphic_identity': 'user',
    }
    id = Column(
        String(64),
        primary_key = True,
        doc = "Unique identifier for the user"
    )
    name = Column(
        String(64),
        nullable = False,
        doc = "First name"
    )
    surname = Column(
        String(64),
        nullable = False,
        doc = "Surname"
    )
    date_of_birth = Column(
        Date,
        nullable = False,
        doc = "Date of birth"
    )
    place_of_birth = Column(
        String(64),
        nullable = False,
        doc = "Place of birth"
    )
    fiscal_code = Column(
        String(16),
        nullable = False,
        unique = True,
        doc = "Personal fiscal code (unique)"
    )
    address = Column(
        String(128),
        nullable = True,
        doc = "Residential address"
    )
    city = Column(
        String(64),
        nullable = True,
        doc = "City of residence"
    )
    province = Column(
        String(32),
        nullable = True,
        doc = "Province/region of residence"
    )
    country = Column(
        String(32),
        nullable = True,
        doc = "Country of residence"
    )
    phone = Column(
        String(32),
        nullable = True,
        doc = "Personal phone number"
    )
    email = Column(
        String(128),
        nullable = True,
        doc = "Personal email address"
    )
    notes = Column(
        String(255),
        nullable = True,
        doc = "Additional notes or comments"
    )
    entity_user = Column(
        String(32),
        nullable = False,
        doc = "Type of user: employee, client, etc."
    )
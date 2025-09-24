from models.base import Base
from sqlalchemy import Column, Float, String


class BusinessEntity(Base):
    """
    Abstract base table for all business entities (suppliers, providers, state entities, stakeholders).
    Table: business_entity (abstract)

    Inherited by:
        - Provider
        - Supplier
        - StateEntity
        - Stakeholder

    Columns:
        id (String, PK): Unique identifier for the entity (UUID or code)
        name (String): Full name or business name of the entity
        vat_number (String, unique): VAT/tax identification code (if applicable)
        address (String): Main office or registered address
        city (String): City of the main office
        province (String): Province/region of the main office
        country (String): Country of the main office
        phone (String): Main contact phone number
        email (String): Main contact email address
        website (String): Website URL (if any)
        rating (Float): Rating or score (optional)
        notes (String): Additional notes or comments
        entity_type (String): Type of entity: supplier, provider, state_entity, stakeholder
    """
    __tablename__ = 'business_entity'
    __mapper_args__ = {
        'polymorphic_on': 'entity_type',
        'polymorphic_identity': 'business_entity',
    }
    id = Column(
        String(64),
        primary_key = True,
        doc = "Unique identifier for the entity (UUID or code)"
    )
    name = Column(
        String(128),
        nullable = False,
        doc = "Full name or business name of the entity"
    )
    vat_number = Column(
        String(32),
        nullable = True,
        unique = True,
        doc = "VAT/tax identification code (if applicable)"
    )
    address = Column(
        String(255),
        nullable = True,
        doc = "Main office or registered address"
    )
    city = Column(
        String(64),
        nullable = True,
        doc = "City of the main office"
    )
    province = Column(
        String(32),
        nullable = True,
        doc = "Province/region of the main office"
    )
    country = Column(
        String(64),
        nullable = True,
        doc = "Country of the main office"
    )
    phone = Column(
        String(32),
        nullable = True,
        doc = "Main contact phone number"
    )
    email = Column(
        String(128),
        nullable = True,
        doc = "Main contact email address"
    )
    website = Column(
        String(128),
        nullable = True,
        doc = "Website URL (if any)"
    )
    rating = Column(
        Float,
        nullable = True,
        doc = "Rating or score (optional)"
    )
    notes = Column(
        String(255),
        nullable = True,
        doc = "Additional notes or comments"
    )
    entity_type = Column(
        String(32),
        nullable = False,
        doc = "Type of entity: supplier, provider, state_entity, stakeholder"
    )
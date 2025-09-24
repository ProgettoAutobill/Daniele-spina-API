from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.businessEntity import BusinessEntity


class Provider(BusinessEntity):
    """
    Provider: Entity providing services or non-goods supplies (e.g., utilities, maintenance, professional services).
    Table: provider
    Inherits: business_entity

    Columns:
        id (String, PK, FK): Primary key, foreign key to business_entity.id
        provider_code (String, unique): Internal/external provider code
        category (String): Provider category (e.g., utilities, services, maintenance)
        zip_code (String): Postal/ZIP code of the main office
        is_certified (String): Certification status (ISO, UNI, etc.)
        payment_terms (String): Standard payment terms
        contact_person (String): Main contact person
    Relationships:
        utility_expenses (relationship): All utility expenses associated with this provider (FK to utility_expense)
        marketing_expenses (relationship): All marketing expenses associated with this provider (FK to marketing_expense)
        facility_expenses (relationship): All facility expenses associated with this provider (FK to facility_expense)
        administrative_expenses (relationship): All administrative expenses associated with this provider (FK to administrative_expense)
        other_expenses (relationship): All other expenses associated with this provider (FK to other_expense)
    """
    __tablename__ = 'provider'
    __mapper_args__ = {
        'polymorphic_identity': 'provider',
    }
    id = Column(
        String(64),
        ForeignKey('business_entity.id'),
        primary_key = True
    )
    provider_code = Column(
        String(32),
        nullable = True,
        unique = True,
        doc = "Internal/external provider code"
    )
    category = Column(
        String(64),
        nullable = True,
        doc = "Provider category (e.g., raw materials, services)"
    )
    zip_code = Column(
        String(16),
        nullable = True,
        doc = "Postal/ZIP code of the main office"
    )
    is_certified = Column(
        String(16),
        nullable = True,
        doc = "Certification status (ISO, UNI, etc.)"
    )
    payment_terms = Column(
        String(64),
        nullable = True,
        doc = "Standard payment terms"
    )
    contact_person = Column(
        String(128),
        nullable = True,
        doc = "Main contact person"
    )
    utility_expenses = relationship(
        'UtilityExpense',
        back_populates = 'utility_provider',
        passive_deletes = True,
        doc = "All utility expenses associated with this provider (set NULL on provider delete)"
    )
    marketing_expenses = relationship(
        'MarketingExpense',
        back_populates = 'marketing_provider',
        passive_deletes = True,
        doc = "All marketing expenses associated with this provider (set NULL on provider delete)"
    )
    facility_expenses = relationship(
        'FacilityExpense',
        back_populates = 'facility_provider',
        passive_deletes = True,
        doc = "All facility expenses associated with this provider (set NULL on provider delete)"
    )
    administrative_expenses = relationship(
        'AdministrativeExpense',
        back_populates = 'administrative_provider',
        passive_deletes = True,
        doc = "All administrative expenses associated with this provider (set NULL on provider delete)"
    )
    other_expenses = relationship(
        'OtherExpense',
        back_populates = 'other_provider',
        passive_deletes = True,
        doc = "All other expenses associated with this provider (set NULL on provider delete)"
    )
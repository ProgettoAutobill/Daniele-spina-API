from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.businessEntity import BusinessEntity


class Supplier(BusinessEntity):
    """
    Supplier: Entity supplying goods/products.
    Table: supplier
    Inherits: business_entity

    Columns:
        id (String, PK, FK): Primary key, foreign key to business_entity.id
        supplier_code (String, unique): Internal/external supplier code
        zip_code (String): Postal/ZIP code of the main office
        product_type (String): Type of products supplied
        preferred (String): Preferred supplier flag (yes/no)
        payment_method (String): Preferred payment method
        contact_person (String): Main contact person
    Relationships:
        purchase_expense (relationship): All purchase expenses associated with this supplier (FK to purchase_expense)
    """
    __tablename__ = 'supplier'
    __mapper_args__ = {
        'polymorphic_identity': 'supplier',
    }
    id = Column(
        String(64),
        ForeignKey('business_entity.id'),
        primary_key = True
    )
    supplier_code = Column(
        String(32),
        nullable = True,
        unique = True,
        doc = "Internal/external supplier code"
    )
    zip_code = Column(
        String(16),
        nullable = True,
        doc = "Postal/ZIP code of the main office"
    )
    product_type = Column(
        String(64),
        nullable = True,
        doc = "Type of products supplied"
    )
    preferred = Column(
        String(16),
        nullable = True,
        doc = "Preferred supplier flag (yes/no)"
    )
    payment_method = Column(
        String(64),
        nullable = True,
        doc = "Preferred payment method"
    )
    contact_person = Column(
        String(128),
        nullable = True,
        doc = "Main contact person"
    )
    purchase_expense = relationship(
        'PurchaseExpense',
        back_populates = 'supplier',
        passive_deletes = True,
        doc = "All purchase expenses associated with this supplier (set NULL on supplier delete)"
    )
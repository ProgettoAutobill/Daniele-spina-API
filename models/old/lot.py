from sqlalchemy import Column, Float, ForeignKey, String

from models.old.product import Product


class Lot(Product):
    """
    Lot: Concrete class for product lots (multiple items grouped together).
    Table: lot
    Inherits: product_entity

    Columns:
        id (String, PK, FK): Primary key, foreign key to product_entity.id
        supplier_id (String): Supplier identifier
        lot_id (String): Lot or batch identifier
        num_prod (Float): Number of products in the lot
    """
    __tablename__ = 'lot'
    __mapper_args__ = {
        'polymorphic_identity': 'lot',
    }
    id = Column(
        String(64),
        ForeignKey('product_entity.id'),
        primary_key=True,
        doc="Primary key for the lot entity (FK to product_entity)"
    )
    supplier_id = Column(
        String(64),
        nullable=True,
        doc="Supplier identifier"
    )
    lot_id = Column(
        String(64),
        nullable=True,
        doc="Lot or batch identifier"
    )
    num_prod = Column(
        Float,
        nullable=True,
        doc="Number of products in the lot"
    )
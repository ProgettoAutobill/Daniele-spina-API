from sqlalchemy import Column, Float, ForeignKey, String

from models.old.baseProduct import BaseProduct


class GroceryProduct(BaseProduct):
    """
    GroceryProduct: Concrete class for grocery products (food, fresh, packaged, etc.).
    Table: grocery_product
    Inherits: base_product

    Columns:
        id (String, PK, FK): Primary key, foreign key to product.id
        origin_country (String): Country of origin for the grocery product
        weight (Float): Weight of the grocery product
        weight_uom (String): Unit of measure for weight (e.g., kg, lb)
    """
    __tablename__ = 'grocery_product'
    __mapper_args__ = {
        'polymorphic_identity': 'grocery_product',
    }
    id = Column(
        String(64),
        ForeignKey('base_product.id'),
        primary_key = True,
        doc = "Primary key for the grocery product (FK to base_product)"
    )
    origin_country = Column(
        String(64),
        nullable = True,
        doc = "Country of origin for the grocery product"
    )
    weight = Column(
        Float,
        nullable = True,
        doc = "Weight of the grocery product"
    )
    weight_uom = Column(
        String(16),
        nullable = True,
        doc = "Unit of measure for weight (e.g., kg, lb)"
    )
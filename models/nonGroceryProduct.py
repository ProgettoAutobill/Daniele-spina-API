from sqlalchemy import Column, ForeignKey, Integer, String
from models.baseProduct import BaseProduct


class NonGroceryProduct(BaseProduct):
    """
    NonGroceryProduct: Concrete class for non-grocery products (electronics, household, etc.).
    Table: non_grocery_product
    Inherits: base_product

    Columns:
        id (String, PK, FK): Primary key, foreign key to product.id
        model (String): Model or version of the product
        material (String): Main material of the product (e.g., plastic, metal)
        dimensions (String): Dimensions of the product (e.g., WxHxD)
        power (String): Power specification (e.g., wattage, voltage)
        warranty_period_months (Integer): Warranty period in months for the non-grocery product
    """
    __tablename__ = 'non_grocery_product'
    __mapper_args__ = {
        'polymorphic_identity': 'non_grocery_product',
    }
    id = Column(
        String(64),
        ForeignKey('base_product.id'),
        primary_key=True,
        doc="Primary key for the non-grocery product (FK to base_product)"
    )
    model = Column(
        String(64),
        nullable=True,
        doc="Model or version of the product"
    )
    material = Column(
        String(64),
        nullable=True,
        doc="Main material of the product (e.g., plastic, metal)"
    )
    dimensions = Column(
        String(64),
        nullable=True,
        doc="Dimensions of the product (e.g., WxHxD)"
    )
    power = Column(
        String(32),
        nullable=True,
        doc="Power specification (e.g., wattage, voltage)"
    )
    warranty_period_months = Column(
        Integer,
        nullable=True,
        doc="Warranty period in months for the non-grocery product"
    )
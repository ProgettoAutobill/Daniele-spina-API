from sqlalchemy import Column, Float, ForeignKey, String
from models.groceryProduct import GroceryProduct


class ScaleProduct(GroceryProduct):
    """
    ScaleProduct: Concrete class for scale/weighable grocery products.
    Table: scale_product
    Inherits: grocery_product

    Columns:
        id (String, PK, FK): Primary key, foreign key to grocery_product.id
        price_weight_uom (String): Unit of measure for price per weight (e.g., €/kg)
        scale_number (Float): Scale number for the product
        plu_code (String): PLU code for the product
        is_weighable (String): If the product is weighable (default True)
        tare_weight (Float): Tare weight of the product
    """
    __tablename__ = 'scale_product'
    __mapper_args__ = {
        'polymorphic_identity': 'scale_product',
    }
    id = Column(
        String(64),
        ForeignKey('grocery_product.id'),
        primary_key = True,
        doc = "Primary key for the scale product (FK to grocery_product)"
    )
    price_weight_uom = Column(
        String(16),
        nullable = True,
        doc = "Unit of measure for price per weight (e.g., €/kg)"
    )
    scale_number = Column(
        Float,
        nullable = True,
        doc = "Scale number for the product"
    )
    plu_code = Column(
        String(32),
        nullable = True,
        doc = "PLU code for the product"
    )
    is_weighable = Column(
        String(5),
        nullable = False,
        default = "True",
        doc = "If the product is weighable"
    )
    tare_weight = Column(
        Float,
        nullable = True,
        doc = "Tare weight of the product"
    )
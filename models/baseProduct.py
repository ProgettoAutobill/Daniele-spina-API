from models.base import Base
from sqlalchemy import Column, Float, String


class BaseProduct(Base):
    """
    Abstract base class for all products.
    Defines common attributes and visual recognition fields.
    Table: product

    Columns:
        id (String): Primary key for the product.
        name_product (String): Name of the product.
        category (String): Category of the product.
        description (String): Description of the product.
        sale_price (Float): Sale price of the product.
        image_url (String): URL or path to the product image (visual recognition).
        color (String): Main color of the product (visual recognition).
        shape (String): Shape or form of the product (visual recognition).
        barcode (String): Barcode or QR code for product identification (unique).
        product_type (String): Type of the product (for polymorphic mapping).
    """
    __tablename__ = 'base_product'
    __mapper_args__ = {
        'polymorphic_identity': 'base_product',
        'polymorphic_on': 'product_type'
    }
    id = Column(
        String(64),
        primary_key = True,
        doc = "Primary key for the product"
    )
    name_product = Column(
        String(128),
        nullable = False,
        doc = "Name of the product"
    )
    category = Column(
        String(64),
        nullable = False,
        default = "Altro",
        doc = "Category of the product"
    )
    description = Column(
        String(255),
        nullable = True,
        doc = "Description of the product"
    )
    sale_price = Column(
        Float,
        nullable = True,
        doc = "Sale price of the product"
    )
    # --- Visual recognition attributes ---
    image_url = Column(
        String(255),
        nullable = True,
        doc = "URL or path to the product image"
    )
    color = Column(
        String(32),
        nullable = True,
        doc = "Main color of the product (for recognition)"
    )
    shape = Column(
        String(32),
        nullable = True,
        doc = "Shape or form of the product (for recognition)"
    )
    barcode = Column(
        String(64),
        nullable = True,
        unique = True,
        doc = "Barcode or QR code for product identification"
    )
    product_type = Column(
        String(50),
        doc = "Type of the product"
    )
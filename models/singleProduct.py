from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.product import Product


class SingleProduct(Product):
    """
    SingleProduct: Concrete class for single product entities (individual items).
    Table: single_product
    Inherits: product_entity

    Columns:
        id (String, PK, FK): Primary key, foreign key to product_entity.id
        validity_info (String): Validity or warranty information
        serial_number (String): Serial number of the product
        expiration_date (String): Expiration date (if applicable)
        batch_code (String): Batch or lot code
        supplier_id (String): Supplier identifier
        barcode (String): Barcode of the product
    """
    __tablename__ = 'single_product'
    __mapper_args__ = {
        'polymorphic_identity': 'single_product',
    }
    id = Column(
        String(64),
        ForeignKey('product_entity.id'),
        primary_key = True,
        doc = "Primary key for the single product entity (FK to product_entity)"
    )
    validity_info = Column(
        String(64),
        nullable = True,
        doc = "Validity or warranty information"
    )
    serial_number = Column(
        String(64),
        nullable = True,
        doc = "Serial number of the product"
    )
    expiration_date = Column(
        String(32),
        nullable = True,
        doc = "Expiration date (if applicable)"
    )
    batch_code = Column(
        String(64),
        nullable = True,
        doc = "Batch or lot code"
    )
    supplier_id = Column(
        String(64),
        nullable = True,
        doc = "Supplier identifier"
    )
    barcode = Column(
        String(64),
        nullable = True,
        doc = "Barcode of the product"
    )
    supplier = relationship(
        'Supplier',
        back_populates = 'single_products',
        foreign_keys = ['SingleProduct.supplier_id'],
        uselist = False,
        doc = "Reference to the supplier of this single product (one-to-one)"
    )
from models.base import Base
from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

class Product(Base):
    """
    Table for all product entities (single products, lots, etc.).
    Table: product_entity

    Columns:
        id (String, PK): Primary key for the product entity.
        model_product_id (String, FK): Foreign key to the product model (BaseProduct).
        purchase_price (Float): Purchase price of the product entity.
        sale_price (Float): Sale price of the product entity.
        quantity (Float): Quantity of product units represented by this entity.
        product_entity_type (String): Polymorphic type for the product entity (single, lot, etc.).
    Relationships:
        goods_transactions (relationship): List of GoodsTransaction objects this product is involved in (many-to-many).
    """
    __tablename__ = 'product_entity'
    __mapper_args__ = {
        'polymorphic_on': 'product_entity_type',
        'polymorphic_identity': 'product_entity'
    }
    id = Column(
        String(64),
        primary_key = True,
        doc = "Primary key for the product entity"
    )
    model_product_id = Column(
        String(64),
        ForeignKey('base_product.id'),
        nullable = False,
        doc = "Foreign key to the product model (BaseProduct)"
    )
    purchase_price = Column(
        Float,
        nullable = True,
        doc = "Purchase price of the product entity"
    )
    sale_price = Column(
        Float,
        nullable = True,
        doc = "Sale price of the product entity"
    )
    quantity = Column(
        Float,
        nullable = True,
        doc = "Quantity of product units represented by this entity"
    )
    notes = Column(
        String(255),
        nullable = True,
        doc = "Additional notes or comments"
    )
    product_entity_type = Column(
        String(50),
        doc = "Polymorphic type for the product entity (single, lot, etc.)"
    )
    model_product = relationship(
        'BaseProduct',
        back_populates = 'products',
        foreign_keys = ['Product.model_product_id'],
        uselist = False,
        doc = "Reference to the product model (BaseProduct) this entity is based on (one-to-one)"
    )
    goods_transactions = relationship(
        'GoodsTransaction',
        secondary = 'goods_transaction_product',
        back_populates = 'products',
        doc = "List of GoodsTransaction objects this product is involved in (many-to-many)"
    )
from database.sessionDB import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class GoodsTransactionProduct(Base):
    """
    Association object for many-to-many relationship between GoodsTransaction and Product.
    Stores expense category for each product in a transaction.
    Table: goods_transaction_product

    Columns:
        goods_transaction_id (String, PK, FK): FK to goods_transaction.id
        product_id (String, PK, FK): FK to product.id
        category (String): Expense category for this product in the transaction
    Relationships:
        goods_transaction (relationship): Reference to the goods transaction associated with this product (FK to goods_transaction)
        product (relationship): Reference to the product associated with this transaction (FK to product)
    """
    __tablename__ = 'goods_transaction_product'
    goods_transaction_id = Column(
        String(64),
        ForeignKey('goods_transaction.id'),
        primary_key = True
    )
    product_id = Column(
        String(64),
        ForeignKey('product_entity.id'),
        primary_key = True
    )
    category = Column(
        String(64),
        nullable = True,
        doc = 'Expense category for this product in the transaction'
    )

    # Relationships (optional, for ORM navigation)
    goods_transaction = relationship(
        'GoodsTransaction',
        back_populates = 'product_links'
    )
    product = relationship(
        'Product',
        back_populates = 'transaction_links'
    )
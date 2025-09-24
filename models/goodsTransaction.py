from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from models.cashFlowEntry import CashFlowEntry


class GoodsTransaction(CashFlowEntry):
    """
    Base class for transactions involving goods (purchases, sales, returns, etc.).
    Table: goods_transaction
    Inherits: cash_flow_entry

    Columns:
        id (String, PK, FK): Unique identifier for the goods transaction (FK to cash_flow_entry)
        payment_date (DateTime): Actual payment date (optional)
    Relationships:
    """
    __tablename__ = 'goods_transaction'
    __mapper_args__ = {
        'polymorphic_identity': 'goods_transaction',
    }
    id = Column(
        String(64),
        ForeignKey('cash_flow_entry.id'),
        primary_key = True,
        doc = "Unique identifier for the goods transaction (FK to cash_flow_entry)"
    )
    payment_date = Column(
        DateTime,
        nullable = True,
        doc = "Actual payment date (optional)"
    )
    product_links = relationship(
        'GoodsTransactionProduct',
        back_populates = 'goods_transaction',
        cascade = 'all, delete-orphan',
        doc = 'Links to products involved in this transaction (many-to-many via association object)'
    )
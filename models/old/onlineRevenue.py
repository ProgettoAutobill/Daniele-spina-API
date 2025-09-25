from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.goodsTransaction import GoodsTransaction


class OnlineRevenue(GoodsTransaction):
    """
    Revenue from online sales, including fees and delivery details.
    Table: online_revenue
    Inherits: goods_transaction

    Columns:
        id (String, PK, FK): Unique identifier for the online revenue (FK to goods_transaction)
        order_id (String, FK): Order identifier on the online platform (FK to order)
        customer_id (String, FK): Reference to the customer (FK to customer)
        date_delivered (DateTime): Date when the order was delivered
        status_delivered (String): Delivery status (e.g., delivered, pending)
        delivery_location (String): Delivery location or address
        payment_date (DateTime): Actual payment date (optional)
    Relationships:
        customer (relationship): Reference to the customer associated with this online sale (FK to customer)
        order (relationship): Reference to the order associated with this online sale (FK to order)
    """
    __tablename__ = 'online_revenue'
    __mapper_args__ = {
        'polymorphic_identity': 'online_revenue',
    }
    id = Column(
        String(64),
        ForeignKey('goods_transaction.id'),
        primary_key = True,
        doc = "Unique identifier for the online revenue (FK to goods_transaction)"
    )
    order_id = Column(
        String(64),
        ForeignKey('order.id'),
        nullable = False,
        doc = "Order identifier on the online platform"
    )
    date_delivered = Column(
        DateTime,
        nullable = True,
        doc = "Date when the order was delivered"
    )
    status_delivered = Column(
        String(32),
        nullable = True,
        doc = "Delivery status (e.g., delivered, pending)"
    )
    delivery_location = Column(
        String(128),
        nullable = True,
        doc = "Delivery location or address"
    )
    order = relationship(
        'Order',
        back_populates = 'online_revenues',
        foreign_keys = ['OnlineRevenue.order_id'],
        doc = "Reference to the order associated with this online sale"
    )
from sqlalchemy import Column, ForeignKey, String

from models.old.goodsTransaction import GoodsTransaction


class ClickCollectRevenue(GoodsTransaction):
    """
    Revenue from click & collect sales (online order, in-store pickup).
    Table: click_collect_revenue
    Inherits: goods_transaction

    Columns:
        id (String, PK, FK): Unique identifier for the click & collect revenue (FK to goods_transaction)
        order_id (String, FK): Order identifier for the click & collect transaction (FK to order)
        customer_id (String, FK): Reference to the customer (FK to customer)
        employee_id (String, FK): Reference to the employee handling the order (FK to employee)
        site_shop_location (String, FK): Shop location for pickup (FK to location)
        status_delivered (String): Status of the delivery/pickup (e.g., delivered, pending)
        payment_date (DateTime): Actual payment date (optional)
    Relationships:
        customer (relationship): Reference to the customer associated with this click & collect sale (FK to customer)
        employee (relationship): Reference to the employee handling the order (FK to employee)
        order (relationship): Reference to the order associated with this click & collect sale (FK to order)
        site_shop_location (relationship): Reference to the shop location for pickup (FK to location)
    """
    __tablename__ = 'click_collect_revenue'
    __mapper_args__ = {
        'polymorphic_identity': 'click_collect_revenue',
    }
    id = Column(
        String(64),
        ForeignKey('goods_transaction.id'),
        primary_key=True,
        doc="Primary key for click & collect revenue (FK to goods_transaction)"
    )
    order_id = Column(
        String(64),
        ForeignKey('order.id'),
        nullable = False,
        doc = "Order identifier for the click & collect transaction"
    )
    employee_id = Column(
        String(64),
        ForeignKey(
            'employee.id',
            ondelete = 'SET NULL'
        ),
        nullable = False,
        doc = "Reference to the employee handling the order (FK to employee)"
    )
    site_shop_location = Column(
        String(128),
        ForeignKey('location.id'),
        nullable = True,
        doc = "Shop location for pickup"
    )
    status_delivered = Column(
        String(32),
        nullable = True,
        doc = "Status of the delivery/pickup"
    )
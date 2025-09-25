from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.goodsTransaction import GoodsTransaction


class SaleRevenue(GoodsTransaction):
    """
    Revenue from the sale of goods/products to customers.
    Table: sale_revenue
    Inherits: goods_transaction

    Columns:
        id (String, PK, FK): Unique identifier for the sale revenue (FK to goods_transaction)
        customer_id (String, FK): Reference to the customer (FK to customer)
        employee_id (String, FK): Reference to the employee (FK to employee)
        discount_applied (Float): Discount applied to the sale (absolute value or percentage)
        system (String): System or POS used for the sale
        cash_register_number (String): Cash register number used for the transaction
        promo_code (String): Promotional code applied to the sale
        payment_date (DateTime): Actual payment date (optional)
    Relationships:
        customer (relationship): Reference to the customer associated with this sale (FK to customer)
        employee (relationship): Reference to the employee associated with this sale (FK to employee)
    """
    __tablename__ = 'sale_revenue'
    __mapper_args__ = {
        'polymorphic_identity': 'sale_revenue',
    }
    id = Column(
        String(64),
        ForeignKey('goods_transaction.id'),
        primary_key=True,
        doc="Primary key for sale revenue (FK to goods_transaction)"
    )
    client_id = Column(
        String(64),
        ForeignKey(
            'client.id',
            ondelete = 'SET NULL'
        ),
        nullable = True,
        doc = "Reference to the client (FK to client)"
    )
    employee_id = Column(
        String(64),
        ForeignKey('employee.id'),
        nullable = True,
        doc = "Reference to the employee (FK to employee)"
    )
    discount_applied = Column(
        Float,
        nullable = False,
        doc = "Discount applied to the sale (absolute value or percentage)"
    )
    system = Column(
        String(64),
        nullable = True,
        doc = "System or POS used for the sale"
    )
    cash_register_number = Column(
        String(32),
        nullable = True,
        doc = "Cash register number used for the transaction"
    )
    promo_code = Column(
        String(64),
        nullable = True,
        doc = "Promotional code applied to the sale"
    )
    customer = relationship(
        'Customer',
        back_populates = 'sale_revenues',
        foreign_keys = ['SaleRevenue.customer_id'],
        doc = "Reference to the customer associated with this sale"
    )
    employee = relationship(
        'Employee',
        back_populates = 'sale_revenues',
        foreign_keys = ['SaleRevenue.employee_id'],
        doc = "Reference to the employee associated with this sale"
    )
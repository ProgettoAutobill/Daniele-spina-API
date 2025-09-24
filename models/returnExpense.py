from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.goodsTransaction import GoodsTransaction


class ReturnExpense(GoodsTransaction):
    """
    Expense for returned goods/products (refunds, returns, etc.).
    Table: return_expense
    Inherits: goods_transaction

    Columns:
        id (String, PK, FK): Unique identifier for the return expense (FK to goods_transaction)
        order_id (String, FK): Order identifier for the return (if any) (FK to order)
        customer_id (String, FK): Reference to the customer (FK to customer)
        employee_id (String, FK): Reference to the employee handling the return (FK to employee)
        return_reason (String): Reason for the return/refund
        payment_date (DateTime): Actual payment date (optional)
    Relationships:
        customer (relationship): Reference to the customer associated with this return (FK to customer)
        employee (relationship): Reference to the employee handling the return (FK to employee)
        order (relationship): Reference to the order associated with this return (FK to order)
    """
    __tablename__ = 'return_expense'
    __mapper_args__ = {
        'polymorphic_identity': 'return_expense',
    }
    id = Column(
        String(64),
        ForeignKey('goods_transaction.id'),
        primary_key = True,
        doc = "Unique identifier for the return expense (FK to goods_transaction)"
    )
    order_id = Column(
        String(64),
        ForeignKey('order.id'),
        nullable = True,
        doc = "Order identifier for the return (if any)"
    )
    employee_id = Column(
        String(64),
        ForeignKey(
            'employee.id',
            ondelete = 'SET NULL'
        ),
        nullable = True,
        doc = "Reference to the employee handling the return (FK to employee)"
    )
    return_reason = Column(
        String(255),
        nullable = True,
        doc = "Reason for the return/refund"
    )
    customer = relationship(
        'Customer',
        back_populates = 'return_expenses',
        foreign_keys = ['ReturnExpense.customer_id'],
        doc = "Reference to the customer associated with this return"
    )
    employee = relationship(
        'Employee',
        back_populates = 'return_expenses',
        foreign_keys = ['ReturnExpense.employee_id'],
        doc = "Reference to the employee handling the return"
    )
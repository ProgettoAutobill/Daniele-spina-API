from sqlalchemy import Column, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.goodsTransaction import GoodsTransaction


class PurchaseExpense(GoodsTransaction):
    """
    Expense for purchasing goods/products from suppliers.
    Table: purchase_expense
    Inherits: goods_transaction

    Columns:
        id (String, PK, FK): Unique identifier for the purchase expense (FK to goods_transaction)
        supplier_id (String, FK): Reference to the supplier (FK to supplier)
        payment_due_date (DateTime): Due date for payment (mandatory)
        payment_date (DateTime): Actual payment date (if null, payment has not been accounted/registered)
        penalty (Float): Penalty for late payment (if applicable)
    Relationships:
        supplier (relationship): Reference to the supplier associated with this expense (FK to supplier)
    """
    __tablename__ = 'purchase_expense'
    __mapper_args__ = {
        'polymorphic_identity': 'purchase_expense',
    }
    id = Column(
        String(64),
        ForeignKey('goods_transaction.id'),
        primary_key = True,
        doc = "Unique identifier for the purchase expense (FK to goods_transaction)"
    )
    supplier_id = Column(
        String(64),
        ForeignKey('supplier.id'),
        nullable = False,
        doc = "Reference to the supplier (FK to supplier)"
    )
    payment_due_date = Column(
        DateTime,
        nullable = False,
        doc = "Due date for payment (mandatory)"
    )
    penalty = Column(
        Float,
        nullable = True,
        doc = "Penalty for late payment (if applicable)"
    )
    supplier = relationship(
        'Supplier',
        back_populates = 'purchase_expenses',
        foreign_keys = ['PurchaseExpense.supplier_id'],
        doc = "Reference to the supplier associated with this expense"
    )
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.revenue import Revenue


class ServiceRevenue(Revenue):
    """
    Revenue not related to product sales or invoicing (e.g., loyalty programs, accessory services, after-sales, etc.).
    Table: service_revenue
    Inherits: cash_flow_entry

    Columns:
        id (String, PK, FK): Unique identifier for the service revenue (FK to cash_flow_entry)
        customer_id (String, FK): Reference to the customer (FK to customer, if applicable)
        employee_id (String, FK): Reference to the employee handling the service (FK to employee)
        service_type (String): Type of service provided (if applicable)
        order_id (String, FK): Order identifier for the service (if any)
        payment_date (DateTime): Actual payment date (if applicable)
    Relationships:
        customer (relationship): Reference to the customer associated with this service revenue (FK to customer)
        employee (relationship): Reference to the employee handling the service (FK to employee)
        order (relationship): Reference to the order associated with this service revenue (FK to order)
    """
    __tablename__ = 'service_revenue'
    __mapper_args__ = {
        'polymorphic_identity': 'service_revenue',
    }
    id = Column(
        String(64),
        ForeignKey('revenue.id'),
        primary_key = True,
        doc = "Primary key for service revenue (FK to revenue)"
    )
    customer_id = Column(
        String(64),
        ForeignKey('client.id', ondelete='SET NULL'),
        nullable = True,
        doc = "Reference to the customer (FK to client, SET NULL on delete)"
    )
    employee_id = Column(
        String(64),
        ForeignKey('employee.id', ondelete='SET NULL'),
        nullable = True,
        doc = "Reference to the employee handling the service (FK to employee, SET NULL on delete)"
    )
    service_type = Column(
        String(64),
        nullable=True,
        doc="Type of service provided (if applicable)"
    )
    order_id = Column(
        String(64),
        ForeignKey('order.id', ondelete='SET NULL'),
        nullable=True,
        doc="Order identifier for the service (if any, SET NULL on delete)"
    )
    client = relationship(
        'Client',
        back_populates = 'service_revenues',
        foreign_keys = ['ServiceRevenue.client_id'],
        passive_deletes=True,
        doc = "Reference to the client associated with this service revenue (SET NULL on client delete)"
    )
    employee = relationship(
        'Employee',
        back_populates = 'service_revenues',
        foreign_keys = ['ServiceRevenue.employee_id'],
        passive_deletes=True,
        doc = "Reference to the employee handling the service (SET NULL on employee delete)"
    )
    order = relationship(
        'Order',
        back_populates = 'service_revenues',
        foreign_keys = ['ServiceRevenue.order_id'],
        passive_deletes=True,
        doc = "Reference to the order associated with this service revenue (SET NULL on order delete)"
    )
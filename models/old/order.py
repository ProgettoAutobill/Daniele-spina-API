from database.sessionDB import Base
from sqlalchemy import Column, Date, Float, ForeignKey, String
from sqlalchemy.orm import relationship


class Order(Base):
    """
    Stores customer orders and related information.
    Table: order

    Columns:
        id (String, PK): Primary key for the order model
        customer_id (String, FK): Customer who placed the order
        fees (Float): Fees charged by the platform or payment provider
        platform (String): Online platform used for the sale (e.g., Amazon, Shopify)
        company_delivered (String): Company responsible for delivery (if different from seller)
        order_date (Date): Date of the order
        notes (String): Additional notes for the order
    Relationships:
        client (relationship): Relationship to Client, back_populates 'orders'.
    """
    __tablename__ = 'order'
    id = Column(
        String(64),
        primary_key = True,
        doc = "Primary key for the order model"
    )
    client_id = Column(
        String(64),
        ForeignKey(
            'client.id',
            ondelete = 'SET NULL'
        ),
        nullable = False,
        doc = "FK to client who placed the order"
    )
    fees = Column(
        Float,
        nullable = False,
        doc = "Fees charged by the platform or payment provider"
    )
    platform = Column(
        String(64),
        nullable = False,
        doc = "Online platform used for the sale (e.g., Amazon, Shopify)"
    )
    company_delivered = Column(
        String(64),
        nullable = True,
        doc = "Company responsible for delivery (if different from seller)"
    )
    order_date = Column(
        Date,
        nullable = True,
        doc = "Date of the order"
    )
    notes = Column(
        String(255),
        nullable = True,
        doc = "Additional notes for the order"
    )
    client = relationship(
        'Client',
        back_populates = 'orders',
        foreign_keys = ['Order.client_id'],
        uselist = False,
        doc = "Reference to the client who placed this order (one-to-one)"
    )
    service_revenue = relationship(
        'ServiceRevenue',
        back_populates = 'order',
        foreign_keys = ['ServiceRevenue.order_id'],
        doc = "All service revenue entries associated with this order (one-to-many)"
    )
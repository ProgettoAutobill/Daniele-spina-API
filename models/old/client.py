from sqlalchemy import Column, Date, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.userBase import UserBase


class Client(UserBase):
    """
    Stores clients of the organization.
    Table: client
    Inherits: user

    Columns:
        id (String, PK, FK): Primary key, foreign key to user.id
        client_code (String, unique): Internal client code or reference
        registration_date (Date): Date of registration as client
    Relationships:
        cards (relationship): All loyalty or membership cards associated with this client
        sale_revenue (relationship): All sale revenue records associated with this client
        service_revenue (relationship): All service revenue records associated with this client
        order (relationship): All orders associated with this client
    """
    __tablename__ = 'client'
    __mapper_args__ = {
        'polymorphic_identity': 'client',
    }
    id = Column(
        String(64),
        ForeignKey('user.id'),
        primary_key = True
    )
    client_code = Column(
        String(32),
        nullable = True,
        unique = True,
        doc = "Internal client code or reference"
    )
    registration_date = Column(
        Date,
        nullable = True,
        doc = "Date of registration as client"
    )
    cards = relationship(
        'Card',
        back_populates = 'client',
        cascade = 'all, delete-orphan',
        doc = "All loyalty or membership cards associated with this client"
    )
    sale_revenue = relationship(
        'SaleRevenue',
        back_populates = 'client',
        passive_deletes = True,
        doc = "All sale revenue records associated with this client (set NULL on client delete)"
    )
    service_revenue = relationship(
        'ServiceRevenue',
        back_populates = 'client',
        passive_deletes = True,
        doc = "All service revenue records associated with this client (set NULL on client delete)"
    )
    order = relationship(
        'Order',
        back_populates = 'client',
        passive_deletes = True,
        doc = "All orders associated with this client (set NULL on client delete)"
    )
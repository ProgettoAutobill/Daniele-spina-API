from database.sessionDB import Base
from sqlalchemy import  Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Card(Base):
    """
    Stores membership or loyalty card information for clients.
    Table: card

    Columns:
        id (String, PK): Unique identifier for the card
        client_id (String, FK): Reference to client.id
        card_number (String, unique): Membership or loyalty card number
        points (Integer): Loyalty or reward points accumulated
        issue_date (Date): Card issue date
        expiry_date (Date): Card expiry date
        status (String): Card status (active, expired, blocked, etc.)
        notes (String): Additional notes or comments
    Relationships:
        client (relationship): Relationship to Client, back_populates 'cards'.
    """
    __tablename__ = 'card'
    id = Column(
        String(64),
        primary_key = True,
        doc = "Unique identifier for the card"
    )
    client_id = Column(
        String(64),
        ForeignKey('client.id'),
        nullable = False,
        doc = "Reference to client.id"
    )
    card_number = Column(
        String(32),
        nullable = False,
        unique = True,
        doc = "Membership or loyalty card number"
    )
    points = Column(
        Integer,
        nullable = True,
        doc = "Loyalty or reward points accumulated"
    )
    issue_date = Column(
        Date,
        nullable = True,
        doc = "Card issue date"
    )
    expiry_date = Column(
        Date,
        nullable = True,
        doc = "Card expiry date"
    )
    status = Column(
        String(16),
        nullable = True,
        doc = "Card status (active, expired, blocked, etc.)"
    )
    notes = Column(
        String(255),
        nullable = True,
        doc = "Additional notes or comments"
    )
    client = relationship(
        'Client',
        back_populates = 'cards',
        foreign_keys = ['Card.client_id'],
        uselist = False,
        doc = "Reference to the client who owns this card (one-to-one)"
    )
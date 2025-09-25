from sqlalchemy import Column, DateTime, ForeignKey, func, String
from sqlalchemy.orm import relationship

from database.sessionDB import Base


class AccessLog(Base):
    """
    Table for logging employee authentication/access events.
    Stores each login/access event with timestamp and reference to the authentication record.
    Table: access_log

    Columns:
        id (String): Unique identifier for the access log entry (PK).
        authentication_id (String): Reference to the authentication record (FK to authentication.id).
        access_time (DateTime): Timestamp of access/login (default: now).
        ip_address (String): IP address of the access (IPv4/IPv6, required).
        user_agent (String): User agent or device info (browser, OS, optional).
    Relationships:
        authentication (relationship): Relationship to Authentication, back_populates 'access_logs'.
    """
    __tablename__ = 'access_log'
    id = Column(
        String(64),
        primary_key=True
    )
    authentication_id = Column(
        String(64),
        ForeignKey('authentication.id'),
        nullable=False,
        doc="FK to authentication"
    )
    access_time = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        doc="Timestamp of access/login"
    )
    ip_address = Column(
        String(45),
        nullable=False,
        doc="IP address of the access (IPv4/IPv6, if available)"
    )
    user_agent = Column(
        String(256),
        nullable=True,
        doc="User agent or device info (browser, OS, if available)"
    )
    authentication = relationship(
        'Authentication',
        back_populates='access_logs',
        uselist=False,
        foreign_keys=['AccessLog.authentication_id'],
        doc="Reference to the authentication record for this access log entry"
    )
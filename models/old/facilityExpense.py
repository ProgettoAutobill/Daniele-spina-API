from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.expense import Expense


class FacilityExpense(Expense):
    """
    FacilityExpense: Facility costs (rent, cleaning, maintenance, repairs, equipment, etc.)
    Table: facility_expense
    Inherits: expense

    Columns:
        facility_provider_id (String, FK): Reference to the facility provider (FK to provider)
        facility_type (String): Type of facility (rental, cleaning, maintenance, repairs, equipment, etc.)
        contract_tax_amount (Float): Total tax/fiscal amount as specified in the facility contract
        location (String, FK): Facility location or address (FK to location)
        area_sqm (Float): Area in square meters
    Relationships:
        facility_provider (relationship): Reference to the facility provider associated with this expense (FK to provider)
    """
    __tablename__ = 'facility_expense'
    __mapper_args__ = {
        'polymorphic_identity': 'facility_expense',
    }
    id = Column(
        String(64),
        ForeignKey('expense.id'),
        primary_key = True,
        doc = "Primary key for facility expense (FK to expense)"
    )
    facility_provider_id = Column(
        String(128),
        ForeignKey(
            'provider.id',
            ondelete= 'SET NULL'
        ),
        nullable = False,
        doc = "Reference to the facility provider (FK to provider)"
    )
    facility_type = Column(
        String(64),
        nullable = True,
        doc = "Type of facility (e.g., rental, cleaning, maintenance, repairs, equipment, etc.)"
    )
    contract_tax_amount = Column(
        Float,
        nullable = True,
        doc = "Total tax/fiscal amount as specified in the facility contract"
    )
    # --- facility specific attributes ---
    location = Column(
        String(128),
        ForeignKey(
            'location.id',
            ondelete = 'SET NULL'
        ),
        nullable = True,
        doc = "Facility location or address"
    )
    area_sqm = Column(
        Float,
        nullable = True,
        doc = "Area in square meters"
    )
    facility_provider = relationship(
        'Provider',
        back_populates = 'facility_expenses',
        foreign_keys = ['FacilityExpense.facility_provider_id'],
        doc = "Reference to the facility provider associated with this expense"
    )
    location = relationship(
        'Location',
        back_populates = 'facility_expenses',
        foreign_keys = ['FacilityExpense.location'],
        doc = "Reference to the facility location or address"
    )
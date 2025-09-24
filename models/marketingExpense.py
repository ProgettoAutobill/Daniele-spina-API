from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.expense import Expense


class MarketingExpense(Expense):
    """
    MarketingExpense: Marketing activities and related costs (advertising, promotions, campaigns, etc.)
    Table: marketing_expense
    Inherits: expense

    Columns:
        marketing_provider_id (String, FK): Reference to the marketing provider (FK to provider)
        marketing_type (String): Type of marketing activity (e.g., online, offline, event, etc.)
        contract_tax_amount (Float): Total tax/fiscal amount as specified in the marketing contract
        impressions (Integer): Number of impressions (for digital campaigns)
        clicks (Integer): Number of clicks (for digital campaigns)
        leads (Integer): Number of leads generated
        conversions (Integer): Number of conversions/sales
    Relationships:
        marketing_provider (relationship): Reference to the marketing provider associated with this expense (FK to provider
    """
    __tablename__ = 'marketing_expense'
    __mapper_args__ = {
        'polymorphic_identity': 'marketing_expense',
    }
    id = Column(
        String(64),
        ForeignKey('expense.id'),
        primary_key = True,
        doc = "Primary key for marketing expense (FK to expense)"
    )
    marketing_provider_id = Column(
        String(128),
        ForeignKey(
            'provider.id',
            ondelete = 'SET NULL'
        ),
        nullable = False,
        doc = "Reference to the marketing provider (FK to provider)"
    )
    marketing_type = Column(
        String(32),
        nullable = False,
        doc = "Type of marketing activity (e.g., online, offline, event, etc.)"
    )
    contract_tax_amount = Column(
        Float,
        nullable = True,
        doc = "Total tax/fiscal amount as specified in the marketing contract (importo fiscale contrattuale, non aliquota)"
    )
    # --- digital marketing specific attributes ---
    impressions = Column(
        Integer,
        nullable = True,
        doc = "Number of impressions (for digital campaigns)"
    )
    clicks = Column(
        Integer,
        nullable = True,
        doc = "Number of clicks (for digital campaigns)"
    )
    leads = Column(
        Integer,
        nullable = True,
        doc = "Number of leads generated"
    )
    conversions = Column(
        Integer,
        nullable = True,
        doc = "Number of conversions/sales"
    )
    marketing_provider = relationship(
        'Provider',
        back_populates = 'marketing_expenses',
        foreign_keys = ['MarketingExpense.marketing_provider_id'],
        doc = "Reference to the marketing provider associated with this expense"
    )
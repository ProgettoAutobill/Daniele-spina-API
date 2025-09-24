from models.base import Base
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class EmployeeContract(Base):
    """
    Stores employee contracts (one-to-many: one employee, many contracts over time).
    Table: employee_contract

    Columns:
        id (String, PK): Primary key for the contract
        employee_id (String, FK): FK to employee
        contract_type (String): Type of contract (e.g., permanent, temporary, internship)
        qualification (String): Professional qualification or level
        salary (Float): Base salary or compensation
        start_date (Date): Contract start date
        end_date (Date): Contract end date (if applicable)
        period_of_probe (Integer): Probation period in days (if applicable)
        income_tax_rate (Float): Income tax rate (%) applied to gross salary
        social_security_rate (Float): Social security contribution rate (%) applied to gross salary
        pension_fund_rate (Float): Pension fund contribution rate (%) applied to gross salary
        other_withholding_rate (Float): Other withholdings rate (%) applied to gross salary (e.g., union, welfare, etc.)
        notes (String): Additional notes or comments about the contract
        employee (relationship): Relationship to Employee
    Relationships:
        employee (relationship): Relationship to Employee, back_populates 'contracts'.
    """
    __tablename__ = 'employee_contract'
    id = Column(
        String(64),
        primary_key = True
    )
    employee_id = Column(
        String(64),
        ForeignKey(
            'employee.id',
            ondelete = 'SET NULL'
        ),
        nullable = False,
        doc = "FK to employee"
    )
    contract_type = Column(
        String(32),
        nullable = True,
        doc = "Type of contract (e.g., permanent, temporary, internship)"
    )
    qualification = Column(
        String(64),
        nullable = True,
        doc = "Professional qualification or level"
    )
    salary = Column(
        Float,
        nullable = True,
        doc = "Base salary or compensation"
    )
    start_date = Column(
        Date,
        nullable = True,
        doc = "Contract start date"
    )
    end_date = Column(
        Date,
        nullable = True,
        doc = "Contract end date (if applicable)"
    )
    period_of_probe = Column(
        Integer,
        nullable = True,
        doc = "Probation period in days (if applicable)"
    )
    income_tax_rate = Column(
        Float,
        nullable = True,
        doc = "Income tax rate (%) applied to gross salary"
    )
    social_security_rate = Column(
        Float,
        nullable = True,
        doc = "Social security contribution rate (%) applied to gross salary"
    )
    pension_fund_rate = Column(
        Float,
        nullable = True,
        doc = "Pension fund contribution rate (%) applied to gross salary"
    )
    other_withholding_rate = Column(
        Float,
        nullable = True,
        doc = "Other withholdings rate (%) applied to gross salary (e.g., union, welfare, etc.)"
    )
    notes = Column(
        String(255),
        nullable = True,
        doc = "Additional notes or comments about the contract"
    )
    employee = relationship(
        'Employee',
        back_populates = 'contracts',
        foreign_keys = ['EmployeeContract.employee_id'],
        uselist = False,
        doc = "Relationship to Employee (one-to-one)"
    )
from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.expense import Expense


class StaffExpense(Expense):
    """
    StaffExpense: Staff expenses such as salaries, contributions, collaborations, etc.
    Table: staff_expense
    Inherits: expense

    Columns:
        employee_id (String, FK): Reference to the employee (FK to employee)
        net_salary (Float): Net salary after taxes and deductions
        social_security (Float): Social security contributions (employer + employee)
        withholding_tax (Float): Withholding tax (income tax withheld at source)
        bonus (Float): Bonus (performance, holiday, etc.)
        overtime (Float): Overtime compensation
        severance_pay (Float): Severance pay (TFR, end-of-service allowance)
        reimbursement (Float): Reimbursements (travel, expenses, etc.)
        meal_voucher (Float): Meal vouchers (lunch tickets, etc.)
        insurance (Float): Insurance (health, accident, etc.)
        fringe_benefit (Float): Fringe benefits (e.g., company car, phone, housing, etc.)
        training_cost (Float): Training and professional development costs (courses, certifications, etc.)
        union_fee (Float): Union fees or dues withheld from salary
        advance_payment (Float): Advance payments on salary
        maternity_leave (Float): Maternity/paternity leave allowance
        sick_leave (Float): Sick leave or injury allowance
        pension_fund (Float): Supplementary pension fund contributions
        welfare_contribution (Float): Corporate welfare contributions
        other_withholdings (Float): Other withholdings (e.g., garnishments, family allowances, etc.)
    """
    __tablename__ = 'staff_expense'
    __mapper_args__ = {
        'polymorphic_identity': 'staff_expense',
    }
    id = Column(
        String(64),
        ForeignKey('expense.id'),
        primary_key = True,
        doc = "Primary key for staff expense (FK to expense)"
    )
    employee_contract_id = Column(
        String(64),
        ForeignKey(
            'employee_contract.id',
            ondelete = 'SET NULL'
        ),
        nullable = False,
        doc = "Reference to the employee contract (FK to employee_contract)"
    )
    net_salary = Column(
        Float,
        nullable = False,
        doc = "Net salary after taxes and deductions"
    )
    social_security = Column(
        Float,
        nullable = True,
        doc = "Social security contributions (employer + employee)"
    )
    withholding_tax = Column(
        Float,
        nullable = True,
        doc = "Withholding tax (income tax withheld at source)"
    )
    bonus = Column(
        Float,
        nullable = True,
        doc = "Bonus (performance, holiday, etc.)"
    )
    overtime = Column(
        Float,
        nullable = True,
        doc = "Overtime compensation"
    )
    severance_pay = Column(
        Float,
        nullable = True,
        doc = "Severance pay (TFR, end-of-service allowance)"
    )
    reimbursement = Column(
        Float,
        nullable = True,
        doc = "Reimbursements (travel, expenses, etc.)"
    )
    meal_voucher = Column(
        Float,
        nullable = True,
        doc = "Meal vouchers (lunch tickets, etc.)"
    )
    insurance = Column(
        Float,
        nullable = True,
        doc = "Insurance (health, accident, etc.)"
    )
    fringe_benefit = Column(
        Float,
        nullable = True,
        doc = "Fringe benefits (e.g., company car, phone, housing, etc.)"
    )
    training_cost = Column(
        Float,
        nullable = True,
        doc = "Training and professional development costs (courses, certifications, etc.)"
    )
    union_fee = Column(
        Float,
        nullable = True,
        doc = "Union fees or dues withheld from salary"
    )
    advance_payment = Column(
        Float,
        nullable = True,
        doc = "Advance payments on salary"
    )
    maternity_leave = Column(
        Float,
        nullable = True,
        doc = "Maternity/paternity leave allowance"
    )
    sick_leave = Column(
        Float,
        nullable = True,
        doc = "Sick leave or injury allowance"
    )
    pension_fund = Column(
        Float,
        nullable = True,
        doc = "Supplementary pension fund contributions"
    )
    welfare_contribution = Column(
        Float,
        nullable = True,
        doc = "Corporate welfare contributions"
    )
    other_withholdings = Column(
        Float,
        nullable = True,
        doc = "Other withholdings (e.g., garnishments, family allowances, etc.)"
    )
    employee_contract = relationship(
        'EmployeeContract',
        back_populates = 'staff_expenses',
        foreign_keys = ['StaffExpense.employee_contract_id'],
        doc = "Reference to the employee contract associated with this expense"
    )
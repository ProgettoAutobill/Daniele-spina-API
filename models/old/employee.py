from sqlalchemy import Column, Date, ForeignKey, String
from sqlalchemy.orm import relationship

from models.old.userBase import UserBase


class Employee(UserBase):
    """
    Stores employees or collaborators in the organization.
    Table: employee
    Inherits: user

    Columns:
        id (String, PK, FK): Primary key, foreign key to user.id
        employee_code (String, unique): Internal employee code or badge number
        hire_date (Date): Date of hiring
        termination_date (Date): Date of termination (if applicable)
        work_phone (String): Work phone number
        work_email (String): Work email address
        role_id (String, FK): Role assigned to the user (FK to role.id, SET NULL on delete)
        location_id (String, FK): Location assigned to the employee (FK to location.id, SET NULL on delete)
        supervisor_id (String, FK): ID of the supervisor/manager (FK to employee.id, SET NULL on delete)
    Relationships:
        location (relationship): Location assigned to the employee (FK to location.id)
        supervisor (relationship): Supervisor/manager of the employee (FK to employee.id)
        authentication (relationship): Authentication details for the employee
        contract (relationship): Employee contract details
        sale_revenue (relationship): All sale revenue records associated with this employee
        click_collect_revenue (relationship): All click-and-collect revenue records associated with this employee
        return_expense (relationship): All return expense records associated with this employee
    """
    __tablename__ = 'employee'
    __mapper_args__ = {
        'polymorphic_identity': 'employee',
    }
    id = Column(
        String(64),
        ForeignKey('user.id'),
        primary_key = True
    )
    employee_code = Column(
        String(32),
        nullable = False,
        unique = True,
        doc = "Internal employee code or badge number (unique)"
    )
    hire_date = Column(
        Date,
        nullable = False,
        doc = "Date of hiring"
    )
    termination_date = Column(
        Date,
        nullable = True,
        doc = "Date of termination (if applicable)"
    )
    work_phone = Column(
        String(32),
        nullable = True,
        doc = "Work phone number"
    )
    work_email = Column(
        String(128),
        nullable = True,
        doc = "Work email address"
    )
    role_id = Column(
        String(64),
        ForeignKey(
            'role.id',
            ondelete = 'SET NULL'
        ),
        nullable = True,
        doc = "Role assigned to the user (FK to role.id, SET NULL on role delete)"
    )
    location_id = Column(
        String(64),
        ForeignKey(
            'location.id',
            ondelete = 'SET NULL'
        ),
        nullable = True,
        doc = "Location assigned to the employee (FK to location.id, SET NULL on location delete)"
    )
    supervisor_id = Column(
        String(64),
        ForeignKey(
            'employee.id',
            ondelete = 'SET NULL'
        ),
        nullable = True,
        doc = "ID of the supervisor/manager (FK to employee.id, SET NULL on supervisor delete)"
    )
    location = relationship(
        'Location',
        back_populates = 'employees',
        foreign_keys = ['Employee.location_id'],
        uselist = False,
        doc = "Reference to the location assigned to the employee (one-to-one)"
    )
    supervisor = relationship(
        'Employee',
        back_populates = 'subordinates',
        foreign_keys = ['Employee.supervisor_id'],
        uselist = False,
        doc = "Reference to the supervisor/manager of the employee (one-to-one)"
    )
    authentication = relationship(
        'Authentication',
        back_populates = 'employee',
        uselist = False,
        cascade = 'all, delete-orphan'
    )
    contract = relationship(
        'EmployeeContract',
        back_populates = 'employee',
        passive_deletes = True,
        uselist = False
    )
    sale_revenue = relationship(
        'SaleRevenue',
        back_populates = 'employee',
        passive_deletes = True,
        doc = "All sale revenue records associated with this employee (set NULL on employee delete)"
    )
    click_collect_revenue = relationship(
        'ClickCollectRevenue',
        back_populates = 'employee',
        passive_deletes = True,
        doc = "All click-and-collect revenue records associated with this employee (set NULL on employee delete)"
    )
    return_expense = relationship(
        'ReturnExpense',
        back_populates = 'employee',
        passive_deletes = True,
        doc = "All return expense records associated with this employee (set NULL on employee delete)"
    )
    service_revenue = relationship(
        'ServiceRevenue',
        back_populates = 'employee',
        passive_deletes = True,
        doc = "All service revenue records associated with this employee (set NULL on employee delete)"
    )
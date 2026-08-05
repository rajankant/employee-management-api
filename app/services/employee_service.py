from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee import EmployeeCreate


class EmployeeService:

    def __init__(self):
        self.repository = EmployeeRepository()

    def create(
        self,
        db: Session,
        employee: EmployeeCreate
    ) -> Employee:

        existing_employee = self.repository.get_by_email(
            db,
            employee.email
        )

        if existing_employee:
            raise ValueError("Employee with this email already exists.")

        return self.repository.create(db, employee)
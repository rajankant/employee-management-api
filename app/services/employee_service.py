from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


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

    def get_all(self, db: Session) -> list[Employee]:
        return self.repository.get_all(db)

    def get_by_id(self, db: Session, employee_id: int) -> Employee | None:
        return self.repository.get_by_id(db, employee_id)

    def update(
        self,
        db: Session,
        employee_id: int,
        employee_data: EmployeeUpdate
    ) -> Employee | None:

        return self.repository.update(
            db,
            employee_id,
            employee_data
        )

    def delete(self, db: Session, employee_id: int) -> bool:

        return self.repository.delete(
            db,
            employee_id
        )

    

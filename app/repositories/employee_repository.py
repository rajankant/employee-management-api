
from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

class EmployeeRepository:

    def create(
            self,
            db: Session,
            employee: EmployeeCreate
    ) -> Employee:

        new_employee = Employee(
            **employee.model_dump()
        )

        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee

    def get_all(self, db: Session) -> list[Employee]:
        return db.query(Employee).all()

    def get_by_id(self, db: Session, employee_id: int) -> Employee | None:
        return db.query(Employee).filter(Employee.id == employee_id).first()

    def get_by_email(
        self,
        db: Session,
        email: str
    ) -> Employee | None:

        return (
            db.query(Employee)
            .filter(Employee.email == email)
            .first()
        )

    def update(
        self,
        db: Session,
        employee_id: int,
        updated_employee: EmployeeUpdate
    ) -> Employee | None:

        employee = self.get_by_id(db, employee_id)

        if not employee:
            return None

        for key, value in updated_employee.model_dump(exclude_unset=True).items():
            setattr(employee, key, value)

        db.commit()
        db.refresh(employee)

        return employee
    def delete(self, db: Session, employee_id: int) -> bool:
        employee = db.query(Employee).filter(Employee.id == employee_id).first()

        if not employee:
            return False

        db.delete(employee)
        db.commit()
        return True


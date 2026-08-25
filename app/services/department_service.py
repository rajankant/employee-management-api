from sqlalchemy.orm import Session

from app.models.department import Department
from app.repositories.department_repository import DepartmentRepository
from app.schemas.department import DepartmentCreate


class DepartmentService:

    def __init__(self):
        self.repository = DepartmentRepository()

    def create(
        self,
        db: Session,
        department: DepartmentCreate
    ) -> Department:

        return self.repository.create(db, department)

    def get_all(
        self,
        db: Session
    ) -> list[Department]:

        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        department_id: int
    ) -> Department | None:

        return self.repository.get_by_id(db, department_id)

    def update(
        self,
        db: Session,
        department_id: int,
        department_data: DepartmentCreate
    ) -> Department | None:

        return self.repository.update(db, department_id, department_data)

    def delete(
        self,
        db: Session,
        department_id: int
    ) -> bool:

        department = self.repository.get_by_id(db, department_id)

        if not department:
            return False

        self.repository.delete(db, department_id)
        return True

    
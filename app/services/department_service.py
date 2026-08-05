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
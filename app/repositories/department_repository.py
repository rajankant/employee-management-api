from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import DepartmentCreate


class DepartmentRepository:

    def create(
        self,
        db: Session,
        department: DepartmentCreate
    ) -> Department:

        new_department = Department(
            **department.model_dump()
        )

        db.add(new_department)
        db.commit()
        db.refresh(new_department)

        return new_department
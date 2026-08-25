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

    def get_all(
        self,
        db: Session
    ) -> list[Department]:

        return db.query(Department).all()

    def get_by_id(
        self,
        db: Session,
        department_id: int
    ) -> Department | None:

        return db.query(Department).filter(Department.id == department_id).first()

    def update(
        self,
        db: Session,
        department_id: int,
        department_data: DepartmentCreate
    ) -> Department | None:

        department = db.query(Department).filter(Department.id == department_id).first()

        if not department:
            return None

        for key, value in department_data.model_dump().items():
            setattr(department, key, value)

        db.commit()
        db.refresh(department)

        return department

    def delete(
        self,
        db: Session,
        department_id: int
    ) -> bool:

        department = db.query(Department).filter(Department.id == department_id).first()

        if not department:
            return False

        db.delete(department)
        db.commit()

        return True

    

    
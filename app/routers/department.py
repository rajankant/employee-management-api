from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.department import (
    DepartmentCreate,
    DepartmentResponse,
)
from app.services.department_service import DepartmentService

router = APIRouter(
    prefix="/departments",
    tags=["Departments"],
)

department_service = DepartmentService()


@router.post(
    "/",
    response_model=DepartmentResponse,
    status_code=201,
)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
):
    return department_service.create(db, department)

@router.get("/",
    response_model=list[DepartmentResponse],
)
def get_all_departments(
    db: Session = Depends(get_db),
):
    return department_service.get_all(db)

@router.get("/{department_id}",
    response_model=DepartmentResponse,
)
def get_department(
    department_id: int,
    db: Session = Depends(get_db),
):
    return department_service.get_by_id(db, department_id)

@router.put("/{department_id}",
    response_model=DepartmentResponse,
)
def update_department(
    department_id: int,
    department_data: DepartmentCreate,
    db: Session = Depends(get_db),
):
    return department_service.update(db, department_id, department_data)

@router.delete("/{department_id}",
    status_code=204,
)
def delete_department(
    department_id: int,
    db: Session = Depends(get_db),
):
    department_service.delete(db, department_id)
    return None


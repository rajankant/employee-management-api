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
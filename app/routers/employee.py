from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.employee import EmployeeCreate
from app.services.employee_service import EmployeeService

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

employee_service = EmployeeService()


@router.post("", status_code=201)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    try:
        return employee_service.create(db, employee)

    except ValueError as e:
        raise HTTPException(
            status_code=409,
            detail=str(e)
        )
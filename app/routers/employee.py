from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.employee import EmployeeCreate, EmployeeResponse, EmployeeUpdate
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

@router.get(
        "",
        response_model=list[EmployeeResponse],
        status_code=200
    )
def get_all_employees(
    db: Session = Depends(get_db)
):
    return employee_service.get_all(db)

# GET /employees/{employee_id}
@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
    status_code=200
)
def get_employee(
    employee_id: int, # Path parameter for the employee ID
    db: Session = Depends(get_db) # Dependency injection for the database session
):
    employee = employee_service.get_by_id(db, employee_id) # Retrieve employee by ID
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.patch(
    "/{employee_id}",
    response_model=EmployeeResponse,
    status_code=200
)
def update_employee(
    employee_id: int,
    employee_data: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    updated_employee = employee_service.update(db, employee_id, employee_data)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

@router.delete(
    "/{employee_id}",
    status_code=200
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    success = employee_service.delete(db, employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {
        "message": "Employee deleted successfully"
    }
    
    
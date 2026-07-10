from fastapi import APIRouter
from app.schemas.employee import EmployeeCreate

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

employees = [
    {
        "id": 1,
        "first_name": "Rajan",
        "last_name": "Kant",
        "Email_id": "rajan.kant@example.com",
        "department": "IT"
    },
    {
        "id": 2,
        "first_name": "Aman",
        "last_name": "Sharma",
        "Email_id": "aman.sharma@example.com",
        "department": "HR"
    }
]

@router.get("")
async def get_employees():
    return employees

@router.post("")
async def create_employee(employee: EmployeeCreate):
    new_employee = {
        "id": len(employees) + 1,
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "Email_id": employee.Email_id,
        "department": employee.department
    }
    employees.append(new_employee)
    return new_employee
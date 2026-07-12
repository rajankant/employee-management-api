from fastapi import APIRouter, HTTPException
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

employees = [
    {
        "id": 1,
        "first_name": "Rajan",
        "last_name": "Kant",
        "email_id": "rajan.kant@example.com",
        "department": "IT"
    },
    {
        "id": 2,
        "first_name": "Aman",
        "last_name": "Sharma",
        "email_id": "aman.sharma@example.com",
        "department": "HR"
    }
]

@router.get("")
async def get_employees():
    return employees

@router.post("", status_code=201)
async def create_employee(employee: EmployeeCreate):
    new_id = max((emp["id"] for emp in employees), default=0) + 1
    new_employee = {
        "id": new_id,
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "email_id": employee.email_id,
        "department": employee.department
    }
    employees.append(new_employee)
    return new_employee

@router.get("/{employee_id}")
async def get_employee(employee_id: int):
    for emp in employees:
        if emp["id"] == employee_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")


@router.patch("/{employee_id}")
async def update_employee(employee_id: int, employee: EmployeeUpdate):
    for emp in employees:
        if emp["id"] == employee_id:
            update_data = employee.model_dump(exclude_unset=True)
            emp.update(update_data)
            return emp

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

@router.delete("/{employee_id}")
async def delete_employee(employee_id: int):
    for emp in employees:
        if emp["id"] == employee_id:
            employees.remove(emp)
            return {"message": "Employee deleted successfully"}
        
    raise HTTPException(status_code=404, detail="Employee not found")

@router.put("/{employee_id}")
async def replace_employee(employee_id: int, employee: EmployeeCreate):
    for emp in employees:
        if emp["id"] == employee_id:
            emp["first_name"] = employee.first_name
            emp["last_name"] = employee.last_name
            emp["email_id"] = employee.email_id
            emp["department"] = employee.department
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app.database import get_db
from app.schemas.department import DepartmentCreate, DepartmentResponse
from app.models.department import Department

router = APIRouter(
    prefix="/departments",
    tags=["departments"],
)

@router.post("/", response_model = DepartmentResponse)
def create_department(
    department: DepartmentCreate, 
    db: Session = Depends(get_db)
):
    new_department = Department(
        name=department.name,
    )

    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return new_department
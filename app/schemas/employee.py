from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email_id: str
    department: str

class EmployeeUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email_id: str | None = None
    department: str | None = None
from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    Email_id: str
    department: str
from fastapi import FastAPI
from app.routers.employee import router as employee_router
from app.routers.department import router as department_router


from app.database import Base, engine
import app.models  # Ensure models are imported so that they are registered with SQLAlchemy

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management API",
    version="1.0.0",
    description="Backend API for Employee Management System",
)

app.include_router(employee_router)
app.include_router(department_router)

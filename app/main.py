from fastapi import FastAPI
from app.routers.employee import router as employee_router

app = FastAPI(
    title="Employee Management API",
    version="1.0.0",
    description="Backend API for Employee Management System",
)

app.include_router(employee_router)

from fastapi import FastAPI
from app.database import database
from app.routers.employee import router as employee_router 
app=FastAPI(
    title="Employee Management System",
    description="This is a simple Employee Management System API built with FastAPI.",
    version="1.0.0",
)
app.include_router(employee_router)
@app.get("/")
async def home():
    await database.command("ping")
    return {"message": "MongoDB is connected sucessfully"}


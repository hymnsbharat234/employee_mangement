from fastapi import FastAPI
from app.database import database
app=FastAPI(
    title="Employee Management System",
    description="This is a simple Employee Management System API built with FastAPI.",
    version="1.0.0",
)
@app.get("/")
async def home():
    await database.command("ping")
    return {"message": "MongoDB is connected sucessfully"}


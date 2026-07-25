from bson import ObjectId
from fastapi import APIRouter, HTTPException
from app.database import database
from app.schemes import Employee, EmployeeUpdate
from app.utils import employee_helper

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],

)
@router.post("/")
async def create_employee(employee: Employee):
    employee_data= employee.model_dump()
    result = await database["employees"].insert_one(employee_data)

    return {
        "message": "Employee created successfully",
        "id": str(result.inserted_id)
        }

@router.get("/")
async def get_employees():
    employees = []
    async for employee in database["employees"].find():
        employees.append(employee_helper(employee))
    return employees

@router.get("/{employee_id}")
async def get_employee(employee_id: str):
    try:
        obj_id = ObjectId(employee_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid employee id")

    employee = await database["employees"].find_one({"_id": obj_id})
    if employee:
        return employee_helper(employee)
    raise HTTPException(status_code=404, detail="Employee not found")

@router.put("/{employee_id}")
async def update_employee(employee_id: str, employee_update: EmployeeUpdate):
    try:
        obj_id = ObjectId(employee_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid employee id")

    update_data = {k: v for k, v in employee_update.model_dump().items() if v is not None}
    if update_data:
        result = await database["employees"].update_one({"_id": obj_id}, {"$set": update_data})
        if result.modified_count:
            return {"message": "Employee updated successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")

@router.delete("/{employee_id}")
async def delete_employee(employee_id: str):
    try:
        obj_id = ObjectId(employee_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid employee id")

    result = await database["employees"].delete_one({"_id": obj_id})
    if result.deleted_count:
        return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")

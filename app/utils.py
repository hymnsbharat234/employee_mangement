from bson import ObjectId
def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "name": employee["name"],
        "email": employee["email"],
        "position": employee["position"],
        "salary": employee["salary"],
        "age": employee["age"],
        "department": employee["department"],
    }
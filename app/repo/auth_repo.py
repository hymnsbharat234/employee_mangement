from app.database import database

class AuthRepository:
    def __init__(self):
        self.collection = database["users"]

    async def create_user(self, user_data: dict) -> str:
        result = await self.collection.insert_one(user_data)
        return str(result.inserted_id)

    async def get_user_by_email(self, email: str) -> dict:
        user = await self.collection.find_one({"email": email})
        return user
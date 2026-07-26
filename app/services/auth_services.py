import os
from fastapi import HTTPException
from dotenv import load_dotenv
from app.repo.auth_repo import AuthRepository
from app.auth.security import hash_password, verify_password
from app.auth.jwt_handler import create_access_token

load_dotenv()
JWT_SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

repo = AuthRepository()

class AuthService:
    async def register_user(self,user):
        existing_user = await repo.get_user_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        user_data = user.model_dump()
        user_data["password"] = hash_password(user_data["password"])
        result = await repo.create_user(user_data)
        return {"message": "User registered successfully", "user_id": result}


    async def login_user(self, email: str, password: str):
        db_user = await repo.get_user_by_email(email)
        if not db_user or not verify_password(password, db_user["password"]):
            raise HTTPException(status_code=401, detail="Invalid email or password")
        access_token = create_access_token(data={"sub": db_user["email"]}, secret_key=JWT_SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": access_token, "token_type": "bearer"}
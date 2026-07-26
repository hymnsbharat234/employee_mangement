from fastapi import APIRouter, HTTPException
from app.schemas.auth import UserRegister
from app.services.auth_services import AuthService
from app.schemas.auth import UserLogin

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

service = AuthService()

@router.post("/register")
async def register_user(user: UserRegister):
    result = await service.register_user(user)
    return result

@router.post("/login")
async def login_user(user: UserLogin):
    return await service.login_user(user.email, user.password)
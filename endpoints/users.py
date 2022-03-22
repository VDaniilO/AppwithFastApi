from typing import List
from fastapi import APIRouter, Depends

from repositories.users import UserRepository
from models.user import User, UserSend
from .depends import get_user_repository

router = APIRouter()

@router.get("/", response_model = List[User])
async def read_user(
    users: UserRepository = Depends(get_user_repository),
    limit: int = 100,
    skip: int = 0):
    return await users.get_user_repository(limit = limit, skip = 0)

@router.post("/", response_model = User)
async def read_user(
    user: UserSend,
    users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)

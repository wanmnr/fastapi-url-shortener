# app/routes/user.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def get_users():
    return [{"id": 1, "name": "John Doe"}]



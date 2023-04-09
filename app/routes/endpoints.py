from fastapi import APIRouter, Request
from typing import List

from app.service.models import User, UserResponse
from app.service.service import UserManagmentService


api = APIRouter()


@api.get("/liveness")
async def liveness():
    return {"HEALTH": "OK"}


@api.get("/users", response_model=List[UserResponse])
async def get_all_users(request: Request):
    return UserManagmentService().get_all_users()


@api.get("/users/{id:path}", response_model=User)
async def get_user_by_id(request: Request, id: str):
    return UserManagmentService().get_user_by_id(user_id=id)


@api.post("/users")
async def create_user(request: Request, user: User):
    return UserManagmentService().create_user(user=user)


@api.put("/users/{id:path}")
async def update_user(request: Request, id: str, user: User):
    return UserManagmentService().update_user(user_id=id, user=user)


@api.delete("/users/{id:path}")
async def delete_user(request: Request, id: str):
    return UserManagmentService().delete_user(user_id=id)

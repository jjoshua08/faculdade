from fastapi import APIRouter
from schemas.user_schema import User
from services.user_service import *

router = APIRouter()
#GET/All users
@router.get("/users")
def list_users():
    return get_all_users_service()

#POST - CREATE USER
@router.post("/users")
def create_user(user: User):
    return create_user_service(user)
    
#GET - USER BY ID
@router.get("/users/{user_id}")
def get_user(user_id: str):
    return get_user_by_id_service(user_id)

#UPDATE
@router.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    return update_user_service(user_id, user)

#DELETE
@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    return delete_user_service(user_id)
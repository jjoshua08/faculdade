from repositories.user_repository import *
from bson import ObjectId

def format_user(user):
    user["_id"] = str(user["_id"])
    return user

def create_user_service(user):
    result = create_user(user.model_dump())
    return {"message": "User created", "id": str(result.inserted_id)}

def get_all_users_service():
    users = get_all_users()
    return [format_user(user) for user in users]

def get_user_by_id_service(user_id):
    try:
        user = get_user_by_id(user_id)
    except:
        return {"error": "Invalid ID"}
    if not user:
        return {"error": "User not found"}
    return format_user(user)

def update_user_service(user_id, user):
    try:
        result = update_user(user_id, user.model_dump())
    except:
        return {"error": "Invalid ID"}
    if result.matched_count == 0:
        return {"error": "User not found"}
    return {"message": "User Updated"}

def delete_user_service(user_id):
    try:
        result = delete_user(user_id)
    except:
        return {"error": "Invalid ID"}
    if result.deleted_count == 0:
        return {"error": "User not found"}
    return {"message": "User deleted"}
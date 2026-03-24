from fastapi import APIRouter
from database import users_collection
from schemas import User

router = APIRouter()

@router.get("/users")
def list_users():
    users = []

    for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)

    return users

#POST - CREATE USER
@router.post("/users")
def create_user(user: User):
    user_dict = user.model_dump()
    result = users_collection.insert_one(user_dict)
    return {
        "message": "User created",
        "id": str(result.inserted_id)
    }

#GET - USER BY ID

@router.get("/users/{user_id}")
def get_user(user_id: str):
    from bson import ObjectId

    user = users_collection.find_one({"_id": ObjectId(user_id)})

    if user:
        user["_id"] = str(user["_id"])  
        return user
    return {"error": "user not found"}

#DELETE
@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    from bson import ObjectId
    user = users_collection.find_one_and_delete({"_id": ObjectId(user_id)})

    if user:
        user["_id"] = str(user["_id"])
        return user
    return {"error": "user not found"}


#UPDATE

@router.put("/users/{user_id}")
def update_user(user_id: str):
    from bson import ObjectId

    user = users_collection.find_one_and_update({"_id": ObjectId(user_id)})

    if user:
        user["_id"] = str(user["_id"])
        return user
    return {"error": "user not found"}
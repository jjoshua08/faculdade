from database import users_collection
from bson import ObjectId

def create_user(user_dict):
    return users_collection.insert_one(user_dict)

def get_all_users():
    return list(users_collection.find())

def get_user_by_id(user_id):
    return users_collection.find_one({"_id": ObjectId(user_id)})

def update_user(user_id, user_dict):
    return users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user_dict}
    )

def delete_user(user_id):
    return users_collection.delete_one(
        {"_id": ObjectId(user_id)}
    )
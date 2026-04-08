from fastapi import APIRouter
from database import cars_collection
from schemas import Car
from bson import ObjectId

router = APIRouter()

@router.get("/cars")
def list_cars():
    cars = []

    for car in cars_collection.find():
        car["_id"] = str(car["_id"])
        cars.append(car)

    return cars

#POST - CREATE USER
@router.post("/cars")
def create_car(car: Car):
    car_dict = car.model_dump()
    result = cars_collection.insert_one(car_dict)
    return {
        "message": "Car created",
        "id": str(result.inserted_id)
    }

#GET - USER BY ID

@router.get("/cars/{car_id}")
def get_car(car_id: str):

    car = cars_collection.find_one({"_id": ObjectId(car_id)})

    if car:
        car["_id"] = str(car["_id"])  
        return car
    return {"error": "car not found"}

#UPDATE
@router.put("/cars/{car_id}")
def update_car(car_id: str, car: Car):
    car_dict = car.model_dump()
    result = cars_collection.update_one(
        {"_id": ObjectId(car_id)},
        {"$set": car_dict}
    )
    if result.matched_count == 0:
        return {"error": "user not found"}
    return {"message": "Car Update"}

#DELETE
@router.delete("/cars/{car_id}")
def delete_car(car_id: str):
    result = cars_collection.delete_one(
        {"_id": ObjectId(car_id)}
    )
    if result.deleted_count == 0:
        return {"error": "car not found"}
    return {"message": "car deleted"}
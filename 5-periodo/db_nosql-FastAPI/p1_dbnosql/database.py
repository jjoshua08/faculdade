from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27018")

client = MongoClient(MONGO_URL)
db = client["biblioteca_db"]
livros_collection = db["livros"]
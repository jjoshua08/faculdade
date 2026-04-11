from database import livros_collection
from bson import ObjectId

def create_livro(livro_dict):
    return livros_collection.insert_one(livro_dict)

def get_all_livros():
    return list(livros_collection.find())

def get_livro_by_id(livro_id):
    return livros_collection.find_one({"_id": ObjectId(livro_id)})

def update_livro(livro_id, livro_dict):
    return livros_collection.update_one(
        {"_id": ObjectId(livro_id)},
        {"$set": livro_dict}
    )

def delete_livro(livro_id):
    return livros_collection.delete_one({"_id": ObjectId(livro_id)})
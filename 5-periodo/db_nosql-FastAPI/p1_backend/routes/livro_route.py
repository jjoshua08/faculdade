from fastapi import APIRouter
from schemas.livro_schema import Livro
from services.livro_service import (
    create_livro_service,
    get_all_livros_service,
    get_livro_by_id_service,
    update_livro_service,
    delete_livro_service
)

router = APIRouter()

@router.get("/livros")
def list_livros():
    return get_all_livros_service()

@router.post("/livros")
def create(livro: Livro):
    return create_livro_service(livro)

@router.get("/livros/{livro_id}")
def get_id(livro_id: str):
    return get_livro_by_id_service(livro_id)

@router.delete("/livros/{livro_id}")
def delete_id(livro_id: str):
    return delete_livro_service(livro_id)
    
@router.patch("/livros/{livro_id}")
def update_id(livro_id: str, livro: Livro):
    return update_livro_service(livro_id, livro)
from fastapi import FastAPI
from routes.livro_route import router

app = FastAPI(title="API de Livros")

app.include_router(router)

@app.get("/")
def home():
    return {"Message": "Catálogo de Livros: FastAPI + MongoDB + Docker"}
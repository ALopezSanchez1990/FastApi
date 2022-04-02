from fastapi import APIRouter

router = APIRouter(
    prefix="/viviendas",
    tags=["viviendas"]
)

@router.get("/")
def listado_viviendas():
    return [
        {
            "Tipo": "Casa",
            "Ciudad": "Atarfe",
            "Titulo": "Casa dos habitaciones"
        },
        {
            "Tipo": "Apartamento",
            "Ciudad": "Albolote",
            "Titulo": "Apartamento dos habitaciones"
        }
    ]
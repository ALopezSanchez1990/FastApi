from fastapi import APIRouter
from app.data_models.viviendas import Vivienda

router = APIRouter(
    prefix="/viviendas",
    tags=["viviendas"]
)


@router.get(
    "/",
    response_description="Listado viviendas",
    response_model=list[Vivienda]
)
def listado_viviendas():
    return [
        {
            "tipo": "Casa",
            "ciudad": "Atarfe",
            "titulo": "Casa dos habitaciones",
            "precio": 5000
        },
        {
            "tipo": "Apartamento",
            "ciudad": "Albolote",
            "titulo": "Apartamento dos habitaciones",
            "precio": 2300
        }
    ]


@router.post("/")
def crear_vivienda(body: Vivienda):
    return {
        "creado": True
    }
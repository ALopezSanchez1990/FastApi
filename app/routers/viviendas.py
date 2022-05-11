from fastapi import APIRouter
import psycopg
from psycopg.rows import class_row
from app.data_models.viviendas import Vivienda
from app.db.database import get_connection, close_connection

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
    conn: psycopg.Connection = get_connection()
    with conn.cursor(row_factory=class_row(Vivienda)) as cursor:
        print("test")
        cursor.execute("SELECT* FROM \"Vivienda\";")
        rows = cursor.fetchall()
        print(rows)
        close_connection(conn)

    return rows

@router.post("/")
def crear_vivienda(body: Vivienda):
    return {
        "creado": True
    }
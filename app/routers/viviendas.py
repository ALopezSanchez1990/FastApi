from msilib.schema import Error
from typing import List
from fastapi import APIRouter, status
import psycopg
from psycopg.rows import class_row
from app.data_models.viviendas import Vivienda, ViviendaPost
from app.db.database import get_connection, close_connection

router = APIRouter(
    prefix="/viviendas",
    tags=["viviendas"]
)

@router.get(
    "/",
    response_description="Listado viviendas",
    #response_model=List[Vivienda]
)
def listado_viviendas():
    conn: psycopg.Connection = get_connection()
    with conn.cursor(row_factory=class_row(Vivienda)) as cursor:
        cursor.execute("SELECT* FROM Vivienda;")
        rows = cursor.fetchall()
        close_connection(conn)
    return rows

@router.get(
    "/{id_vivienda}",
    response_description="Get Vivienda por id",
    #response_model=Vivienda
)
def get_vivienda_por_id(id_vivienda: int):
    conn: psycopg.Connection = get_connection()
    with conn.cursor(row_factory=class_row(Vivienda)) as cursor:
        cursor.execute("Select * FROM Vivienda WHERE id = %s", [id_vivienda])
        data: List[Vivienda] = cursor.fetchone()
        close_connection(conn)
    return data

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_vivienda(vivienda: ViviendaPost):
    conn: psycopg.Connection = get_connection()
    with conn.cursor() as cursor:
        try: 
            cursor.execute("INSERT INTO Vivienda (titulo, descripcion) VALUES (%s, %s)",
                (vivienda.titulo, vivienda.descripcion,))
            conn.commit()
            return {
                "created": True
            }
        except Exception as e: 
            raise Error(e)
        finally:
            close_connection(conn)

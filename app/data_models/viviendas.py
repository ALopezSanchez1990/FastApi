from dataclasses import dataclass

@dataclass
class Vivienda:
    id: int 
    descripcion: str
    titulo: str | None = None

@dataclass
class ViviendaPost:
    descripcion: str
    titulo: str | None

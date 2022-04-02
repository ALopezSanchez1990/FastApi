from fastapi import FastAPI
from .routers import viviendas

app = FastAPI()
app.include_router(viviendas.router)

@app.get("/")
def root():
    return {
        "message": "Hello World"
    }
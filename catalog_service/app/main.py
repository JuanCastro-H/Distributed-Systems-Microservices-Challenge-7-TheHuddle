from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine

from app.models.movie_model import Movie

from app.routes.movie_routes import router as movie_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(movie_router)


@app.get("/")
def root():

    return {
        "message": "Catalog Service Running"
    }
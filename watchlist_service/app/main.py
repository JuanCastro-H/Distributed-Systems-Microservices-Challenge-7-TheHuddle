from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine

from app.models.watchlist_model import Watchlist

from app.routes.watchlist_routes import router as watchlist_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(watchlist_router)


@app.get("/")
def root():

    return {
        "message": "Watchlist Service Running"
    }
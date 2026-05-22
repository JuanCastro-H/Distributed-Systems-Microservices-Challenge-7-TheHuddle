# --- Importar enrutador y manejo de errores ---
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

# --- importar sesion actual ---
from sqlalchemy.orm import Session

# --- Importar tabla de movies ---
from app.models.movie_model import Movie

# --- Obtener schema para la creacion y respuesta de una movie ---
from app.schemas.movie_schema import MovieCreate
from app.schemas.movie_schema import MovieResponse

# --- Traer plantilla de sesiones ---
from app.database.connection import SessionLocal

# --- Traer jwt ---
from app.core.security import verify_token

from app.schemas.movie_schema import MovieUpdate

# --- Inicializar Router ---
router = APIRouter(
    prefix="/catalog",
    tags=["Catalog"]
)

# --- Obtener BD
def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


# --- Introducir peliculas a la plataforma ---
@router.post("/movies",response_model=MovieResponse)
def create_movie(
    movie_data: MovieCreate,
    user_id: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    movie = Movie(
        title=movie_data.title,
        genre=movie_data.genre,
        rating=movie_data.rating
    )

    db.add(movie)

    db.commit()

    db.refresh(movie)

    return movie


# --- Obtener lista de peliculas  cargadas ---
@router.get("/movies",response_model=list[MovieResponse])
def get_movies(
    db: Session = Depends(get_db)
):

    return db.query(Movie).all()


@router.get("/movies/{movie_id}",response_model=MovieResponse)
def get_movie(
    movie_id: int,
    db: Session = Depends(get_db)
):

    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()

    if not movie:

        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    return movie


@router.delete("/movies/{movie_id}")
def delete_movie(
    movie_id: int,
    user_id: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()

    if not movie:

        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    db.delete(movie)

    db.commit()

    return {
        "message": "Movie deleted successfully"
    }


@router.put(
    "/movies/{movie_id}",
    response_model=MovieResponse
)
def update_movie(
    movie_id: int,
    movie_data: MovieUpdate,
    user_id: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()

    if not movie:

        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    movie.title = movie_data.title
    movie.genre = movie_data.genre
    movie.rating = movie_data.rating

    db.commit()

    db.refresh(movie)

    return movie
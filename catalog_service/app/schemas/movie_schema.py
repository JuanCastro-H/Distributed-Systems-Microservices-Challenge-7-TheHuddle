from pydantic import BaseModel

# --- Schema para la obtencion de datos ---
class MovieCreate(BaseModel):

    title: str

    genre: str

    rating: float


# --- Schema de respuesta para el cliente ---
class MovieResponse(MovieCreate):

    id: int

    class Config:

        from_attributes = True


# --- Schema para actualizar una pelicula ---

class MovieUpdate(BaseModel):

    title: str

    genre: str

    rating: float
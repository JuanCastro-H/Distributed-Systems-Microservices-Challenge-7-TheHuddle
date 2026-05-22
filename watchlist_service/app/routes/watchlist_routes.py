from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.schemas.watchlist_schema import WatchlistCreate
from app.schemas.watchlist_schema import WatchlistResponse

from app.database.dependencies import get_db

from app.services.watchlist_service import WatchlistService

from app.core.security import verify_token


router = APIRouter(
    prefix="/watchlist",
    tags=["Watchlist"]
)


@router.post("",response_model=WatchlistResponse)
def add_to_watchlist(
    watchlist_data: WatchlistCreate,
    user_id: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    return WatchlistService.add_movie_to_watchlist(
        db,
        int(user_id),
        watchlist_data.movie_id
    )


@router.get("",response_model=list[WatchlistResponse])
def get_watchlist(
    user_id: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    return WatchlistService.get_watchlist(
        db,
        int(user_id)
    )


@router.delete("/{movie_id}")
def remove_from_watchlist(
    movie_id: int,
    user_id: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    return WatchlistService.remove_movie_from_watchlist(
        db,
        int(user_id),
        movie_id
    )


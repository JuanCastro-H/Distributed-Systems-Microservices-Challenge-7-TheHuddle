import httpx

from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.repositories.watchlist_repository import WatchlistRepository


class WatchlistService:


    @staticmethod
    def add_movie_to_watchlist(
        db: Session,
        user_id: int,
        movie_id: int
    ):

        try:

            response = httpx.get(
                f"http://catalog_service:8000/catalog/movies/{movie_id}"
            )

            if response.status_code != 200:

                raise HTTPException(
                    status_code=404,
                    detail="Movie not found"
                )

        except Exception:

            raise HTTPException(
                status_code=500,
                detail="Catalog service unavailable"
            )


        return WatchlistRepository.create_watchlist_item(
            db,
            user_id,
            movie_id
        )


    @staticmethod
    def get_watchlist(
        db: Session,
        user_id: int
    ):

        return WatchlistRepository.get_user_watchlist(
            db,
            user_id
        )
    

    @staticmethod
    def remove_movie_from_watchlist(
        db: Session,
        user_id: int,
        movie_id: int
    ):

        watchlist_item = WatchlistRepository.get_watchlist_item(
            db,
            user_id,
            movie_id
        )

        if not watchlist_item:

            raise HTTPException(
                status_code=404,
                detail="Movie not found in watchlist"
            )

        WatchlistRepository.delete_watchlist_item(
            db,
            watchlist_item
        )

        return {
            "message": "Movie removed from watchlist"
        }
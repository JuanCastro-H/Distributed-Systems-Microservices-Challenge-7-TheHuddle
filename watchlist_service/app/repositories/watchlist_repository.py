from sqlalchemy.orm import Session

from app.models.watchlist_model import Watchlist


class WatchlistRepository:


    @staticmethod
    def create_watchlist_item(
        db: Session,
        user_id: int,
        movie_id: int
    ):

        watchlist = Watchlist(
            user_id=user_id,
            movie_id=movie_id
        )

        db.add(watchlist)

        db.commit()

        db.refresh(watchlist)

        return watchlist


    @staticmethod
    def get_user_watchlist(
        db: Session,
        user_id: int
    ):

        return db.query(Watchlist).filter(
            Watchlist.user_id == user_id
        ).all()
    

    @staticmethod
    def get_watchlist_item(
        db: Session,
        user_id: int,
        movie_id: int
    ):

        return db.query(Watchlist).filter(
            Watchlist.user_id == user_id,
            Watchlist.movie_id == movie_id
        ).first()


    @staticmethod
    def delete_watchlist_item(
        db: Session,
        watchlist_item: Watchlist
    ):

        db.delete(watchlist_item)

        db.commit()
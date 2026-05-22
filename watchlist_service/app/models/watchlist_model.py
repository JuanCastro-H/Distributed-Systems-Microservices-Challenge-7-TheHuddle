from sqlalchemy import Column
from sqlalchemy import Integer

from app.database.base import Base


class Watchlist(Base):

    __tablename__ = "watchlist"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)

    movie_id = Column(Integer, nullable=False)
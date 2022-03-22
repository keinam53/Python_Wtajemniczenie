from types import TracebackType
from typing import Type, Optional

from logger import log_error
from new_movies.movie_service import MovieService


class MovieServiceConnection:
    def __init__(self, movie_service: MovieService) -> None:
        self.movie_service = movie_service

    def __enter__(self) -> MovieService:
        self.movie_service.connect()
        return self.movie_service

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[Type[BaseException]],
                 exc_tb: Optional[Type[TracebackType]]) -> None:
        if exc_type:
            log_error(f'Błąd: {exc_val}')
        self.movie_service.close()

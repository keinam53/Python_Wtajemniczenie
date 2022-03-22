import random
from types import TracebackType
from typing import Any, Type, Optional

from logger import log_error


class MovieService:
    def connect(self) -> None:
        print("Connecting...")

    def get_movie(self) -> str:
        movie_number = random.randint(1, 100)
        if movie_number % 10 == 0:
            raise ValueError("Ops!")
        return f"Movie({movie_number})"

    def close(self) -> None:
        print("Closing...")


class MovieServiceConnection:
    def __init__(self) -> None:
        self.movie_service = MovieService()

    def __enter__(self) -> MovieService:
        self.movie_service.connect()
        return self.movie_service

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[Type[BaseException]],
                 exc_tb: Optional[Type[TracebackType]]) -> None:
        if exc_type:
            log_error(f'Błąd: {exc_val}')
        self.movie_service.close()

from contextlib import contextmanager
from typing import Iterator

from new_movies import logger


class RemoteServiceError(Exception):
    pass


@contextmanager
def error_handling() -> Iterator[None]:
    try:
        yield
    except BrokenPipeError:
        logger.log_error('BrokenPipeError')
        raise RemoteServiceError("Przerwane połączenie")
    except ConnectionError:
        logger.log_error('ConnectionError')
        raise RemoteServiceError("Nie można się połączyć")
    except TimeoutError:
        logger.log_error('TimeoutError')
        raise RemoteServiceError("Zbyt długi czas łączenia")

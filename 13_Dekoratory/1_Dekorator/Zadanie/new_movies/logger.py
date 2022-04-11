from collections.abc import Callable
from typing import TypeVar, Any, cast

F = TypeVar("F", bound=Callable[..., Any])


def show_name(func: F) -> F:
    def function() -> Any:
        log_info(f'Wywołano funkcję: {func.__name__}')
        return func()

    return cast(F, function)


def log_info(message: str) -> None:
    print(f"[INFO]: {message}")

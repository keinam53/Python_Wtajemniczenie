from collections.abc import Callable
from typing import TypeVar, Any, cast

F = TypeVar("F", bound=Callable[..., Any])


def log_info(message: str) -> None:
    print(f"[INFO]: {message}")


def show_name(func: F) -> F:
    def function(*args: Any, **kwargs: Any) -> Any:
        log_info(f'Wywołano funkcję: {func.__name__}')
        return func(*args, **kwargs)

    return cast(F, function)

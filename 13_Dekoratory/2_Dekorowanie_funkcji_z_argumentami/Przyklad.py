from collections.abc import Callable
from typing import Any, TypeVar, cast


F = TypeVar('F', bound=Callable[..., Any])


def talkative(func: F) -> F:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print('Funkcja startuje!')
        result = func(*args, **kwargs)
        print(f'Wynik to: {result}')
        print('Pa pa')
        return result
    return cast(F, wrapper)


@talkative
def multiply_by_two(number: int) -> int:
    return number * 2


# multiply_by_two = talkative(multiply_by_two) #Działa tak samo jak @


def run() -> None:
    result = multiply_by_two(5)
    print(result)


if __name__ == '__main__':
    run()

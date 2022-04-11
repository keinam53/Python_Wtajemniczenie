import random
from collections.abc import Callable
from typing import Any, TypeVar, cast

F = TypeVar('F', bound=Callable[..., Any])


def goodbye(func: F) -> F:
    def func_with_goodbye() -> Any:
        result = func()
        print('Goodbye')
        print(10 * '-')
        return result

    return cast(F, func_with_goodbye)


@goodbye
def say_hello() -> None:
    print('Hello')


@goodbye
def random_number() -> int:
    print('Random number...')
    return random.randint(0, 99)


def run() -> None:
    say_hello()
    random_value = random_number()
    print(random_value)


if __name__ == '__main__':
    run()

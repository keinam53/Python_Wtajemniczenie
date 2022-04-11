import random
from collections.abc import Callable


def goodbye(func: Callable) -> Callable[[], None]:
    def say_goodbye() -> None:
        print('Goodbye')
    return say_goodbye


@goodbye
def say_hello() -> None:
    print('Hello')


@goodbye
def random_number() -> int:
    print('Random number...')
    return random.randint(0, 99)


def run() -> None:
    say_hello()
    random_number()
    random_value = random_number()
    print(random_value)


if __name__ == '__main__':
    run()

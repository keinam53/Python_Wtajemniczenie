from collections.abc import Generator


def number_generator(max_number: int) -> Generator[int, None, None]:
    number = 0
    while number < max_number:
        number += 1
        yield number


def run() -> None:
    generator_iterator_7 = number_generator(max_number=7)
    generator_iterator_5 = number_generator(max_number=5)

    for number in generator_iterator_5:
        print(number)

    print(10 * '-')
    print(next(generator_iterator_7))
    print(next(generator_iterator_7))
    print(10 * '-')

    for number in number_generator(max_number=4):
        print(number)


if __name__ == '__main__':
    run()

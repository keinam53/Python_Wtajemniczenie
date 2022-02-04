def fibonacci_rek(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci_rek(number - 2) + fibonacci_rek(number - 1)


def fibonacci_iter(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    przed_poprzedni = 0
    poprzedni = 1
    wynik = None

    for aktualny in range(2, number + 1):
        wynik = przed_poprzedni + poprzedni
        przed_poprzedni = poprzedni
        poprzedni = wynik
    return wynik


def run():
    print(fibonacci_rek(3))
    print(fibonacci_rek(14))

    print(fibonacci_iter(3))
    print(fibonacci_iter(14))


if __name__ == '__main__':
    run()

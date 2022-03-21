def silnia_rek(number):
    if number == 0:
        return 1
    return number * silnia_rek(number - 1)


print(silnia_rek(5))


def silnia_iter(number):
    if number == 0:
        return 1
    wynik = 1
    for aktualna_iter in range(1, number + 1):
        wynik = wynik * aktualna_iter
    return wynik


print(silnia_iter(6))


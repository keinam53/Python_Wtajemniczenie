def sprawdz_zdolnosc(kredyt, mieszkanie, *, max_ltv=0.8):
    ltv = kredyt / mieszkanie
    return ltv <= max_ltv


def wypisz(decyzja):
    if decyzja:
        print('Możesz wziąć kredyt')
    else:
        print('Nie możesz')


def run_example():
    kredyt = int(input('Podaj wartość kredytu: '))
    mieszkanie = int(input('Podaj wartość mieszkania: '))
    decyzja = sprawdz_zdolnosc(kredyt, mieszkanie, max_ltv=0.86)

    wypisz(decyzja)


if __name__ == '__main__':
    run_example()

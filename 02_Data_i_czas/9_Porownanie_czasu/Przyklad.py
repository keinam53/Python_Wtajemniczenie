from datetime import datetime, time


def run():
    aktualny_czas = datetime.now().time()
    print(aktualny_czas)
    moment_pozniej = datetime.now().time()
    print(moment_pozniej)
    print('Aktualny czas = Aktualny czas:', aktualny_czas == moment_pozniej)

    koniec_lekcji_gim = time(15, 30)
    koniec_lekcji_lo = time(17)
    print('Koniec lekcji w gimnazjum < koniec lekcji w LO:', koniec_lekcji_gim < koniec_lekcji_lo)


if __name__ == '__main__':
    run()

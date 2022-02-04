from datetime import date


def run():
    marzec_2022 = date(year=2022, month=3, day=20)
    maj_2000 = date(2000, 5, 19)
    przyszla = date(year=5984, month=8, day=27)

    print(marzec_2022)
    print(maj_2000)
    print(przyszla)

    #Właściwości daty
    nastepne_urodziny = date(year=2022, month=8, day=27)
    print(f'Dzień: {nastepne_urodziny.day}, Miesiąc: {nastepne_urodziny.month}, Rok: {nastepne_urodziny.year}')


if __name__ == '__main__':
    run()

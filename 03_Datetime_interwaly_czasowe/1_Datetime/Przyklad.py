from datetime import datetime


def run():
    data_czas = datetime(year=2022, month=1, day=20, hour=13, minute=40, second=16)
    print(data_czas)
    data_czas = datetime(2022, 1, 20, 13, 40, 16)
    print(data_czas)

    print(f'Rok: {data_czas.year} Miesiąc: {data_czas.month} Dzień: {data_czas.day} '
          f'Godzina: {data_czas.hour} Minuta: {data_czas.minute} Sekunda: {data_czas.second}')

    piec_godz_pozniej = data_czas.replace(hour=data_czas.hour + 5)
    print(f'{data_czas} Pięć godzin później będzie: {piec_godz_pozniej}')


if __name__ == '__main__':
    run()

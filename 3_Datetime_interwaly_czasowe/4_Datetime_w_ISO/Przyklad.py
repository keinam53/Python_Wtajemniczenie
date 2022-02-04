from datetime import datetime


def run():
    data_czas_input = input('Podaj datę i czas w formacie (YYYY-MM-DD hh:mm:ss): ')
    data_czas = datetime.fromisoformat(data_czas_input)
    print(f'Rok: {data_czas.year}')
    print(f'Miesiąc: {data_czas.month}')
    print(f'Dzień: {data_czas.day}')
    print(f'Godzina: {data_czas.hour}')
    print(f'Minuta: {data_czas.minute}')
    print(f'Sekunda: {data_czas.second}')


if __name__ == '__main__':
    run()

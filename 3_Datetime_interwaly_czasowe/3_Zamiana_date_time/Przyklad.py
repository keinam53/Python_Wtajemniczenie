from datetime import datetime


def run():
    data_czas = datetime(2022, 1, 21, 18, 46, 39)
    print(f'Aktualna data i czas: {data_czas} Typ: {type(data_czas)}')

    data = data_czas.date()
    print(f'Aktualna data: {data} Typ: {type(data)}')

    czas = data_czas.time()
    print(f'Aktualny czas: {czas} Typ: {type(czas)}')


if __name__ == '__main__':
    run()

from datetime import datetime


def run():
    data_czas = datetime(2022, 1, 21, 18, 46, 39)
    print(f'Aktualna data i czas: {data_czas} Typ: {type(data_czas)}')
    data_czas_str = data_czas.isoformat()
    print(f'Aktualna data i czas: {data_czas_str} Typ: {type(data_czas)}')
    print(data_czas.isoformat(sep='*'))


if __name__ == '__main__':
    run()

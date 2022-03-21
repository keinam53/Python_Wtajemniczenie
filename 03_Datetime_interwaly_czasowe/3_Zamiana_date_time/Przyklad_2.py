from datetime import datetime, date, time


def run():
    data = date(2022, 1, 21)
    czas = time(18, 46, 39)
    print(f'Aktualna data: {data} Typ: {type(data)}')
    print(f'Aktualny czas: {czas} Typ: {type(czas)}')

    data_czas = datetime.combine(date=data, time=czas)
    print(f'Aktualna data i czas: {data_czas} Typ: {type(data_czas)}')


if __name__ == '__main__':
    run()

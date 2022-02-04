from datetime import date


def run():
    urodziny = date(year=2022, month=8, day=27)
    przyszle_urodziny = date(year=urodziny.year + 1, month=urodziny.month, day=urodziny.day)

    print(urodziny)
    print(przyszle_urodziny)

    dzien_po_uro = urodziny.replace(day=urodziny.day + 1)
    print(dzien_po_uro)


if __name__ == '__main__':
    run()
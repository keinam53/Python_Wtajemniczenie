from datetime import timedelta, date


def run():
    urodziny = date(year=1994, month=8, day=27)
    imieniny = date(year=1994, month=1, day=19)

    urodziny_imieniny_interwal = urodziny - imieniny
    imieniny_urodziny_interwal = imieniny - urodziny

    print(f'urodziny_imieniny_interwal: {urodziny_imieniny_interwal}')
    print(f'imieniny_urodziny_interwal: {imieniny_urodziny_interwal}')
    print(urodziny_imieniny_interwal * 2)

    print(imieniny + urodziny_imieniny_interwal == urodziny)
    print(imieniny + urodziny_imieniny_interwal * 3 > urodziny)
    print(urodziny_imieniny_interwal > timedelta(days=5))

    dzien_po_urodzinach = urodziny + timedelta(days=1)
    print(dzien_po_urodzinach)


if __name__ == '__main__':
    run()

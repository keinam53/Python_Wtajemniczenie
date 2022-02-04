from datetime import date


def run():
    data = date(2022, 1, 16)
    print(f'16. 01, 2022 toordinal: ', data.toordinal())
    print(f'16. 01, 2022 isocalendar: ', data.isocalendar())


if __name__ == '__main__':
    run()

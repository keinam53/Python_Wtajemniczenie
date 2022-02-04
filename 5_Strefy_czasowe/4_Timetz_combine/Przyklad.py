from datetime import datetime


def run():
    data_czas_isoformat = datetime.fromisoformat("2022-01-26 18:04:38+01:00")
    print(data_czas_isoformat)
    print(data_czas_isoformat.time())
    print(data_czas_isoformat.timetz())


if __name__ == '__main__':
    run()

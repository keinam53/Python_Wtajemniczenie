from datetime import datetime, time


def run():
    data_czas_isoformat = datetime.fromisoformat("2022-01-26 18:04:38+01:00")
    print(data_czas_isoformat)
    print(data_czas_isoformat.tzinfo)

    czas_isoformat = time.fromisoformat("14:35:54+01:00")
    print(czas_isoformat)
    print(czas_isoformat.tzinfo)


if __name__ == '__main__':
    run()

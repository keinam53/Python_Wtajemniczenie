from datetime import date


def run():
    data = date.fromtimestamp(1_610_000_000)
    print(data)


if __name__ == '__main__':
    run()

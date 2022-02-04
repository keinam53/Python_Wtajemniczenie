from datetime import datetime, time


def run():
    aktualny_czas = datetime.now().time()
    print(aktualny_czas)
    print(aktualny_czas.isoformat())

    czas_input = input('Podaj czas w formacie HH:MM:SS: ')
    czas = time.fromisoformat(czas_input)
    print(f'Godzina: {czas.hour} Minuta: {czas.minute} Sekunda: {czas.second}')


if __name__ == '__main__':
    run()

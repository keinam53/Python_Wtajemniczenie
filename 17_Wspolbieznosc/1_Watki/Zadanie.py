import random
import threading


def srednia() -> None:
    liczby = []
    for i in range(10):
        liczby.append(random.randint(0, 100))
    wynik = sum(liczby) / 10
    print(f'{liczby}\nŚrednia liczb: {wynik}\n')


def run() -> None:
    for _ in range(10):
        threading.Thread(target=srednia).start()


if __name__ == '__main__':
    run()

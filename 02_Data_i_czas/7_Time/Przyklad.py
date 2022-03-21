from datetime import time


def run():
    start_lekcji = time(hour=8, minute=15, second=0)
    print(f'Lekcje zaczynają się o {start_lekcji}')

    start_lekcji = time(9, 15, 0)
    print(f'Lekcje zaczynają się o {start_lekcji}')

    start_lekcji = time(hour=8, minute=15, second=0)
    print(f'Lekcje zaczynają się o {start_lekcji}')
    start_lekcji_lo = start_lekcji.replace(start_lekcji.hour + 1)
    print(f'Lekcje w LO zaczynają się godzinę później czyli o {start_lekcji_lo}')


if __name__ == '__main__':
    run()

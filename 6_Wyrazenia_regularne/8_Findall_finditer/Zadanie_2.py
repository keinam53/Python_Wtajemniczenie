import re


def run():
    tekst = '"To jest tekst, który ma adresy email: mariusz@wp.com oraz Przyklad@onet.pl"'
    dopasowanie(tekst)


def dopasowanie(tekst):
    pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")
    emaile = pattern.finditer(tekst)
    for email in emaile:
        print(10 * '-')
        print(email.group())
        wypisanie(email)


def wypisanie(dopasowanie):
    print(f'Nazwa: {dopasowanie[0]}')
    print(f'Domena: {dopasowanie[1]}')
    print(f'Rozszeżenie: {dopasowanie[2]}')
    print(f'Znaleziony na indeksach od: {dopasowanie.start()} do {dopasowanie.end()}')


if __name__ == "__main__":
    run()

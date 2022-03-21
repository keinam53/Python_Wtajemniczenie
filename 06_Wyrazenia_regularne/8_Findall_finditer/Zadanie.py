import re


def run():
    tekst = '"To jest tekst, który ma adresy email: mariusz@wp.com oraz Przyklad@onet.pl"'
    dopasowanie(tekst)


def dopasowanie(tekst):
    pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")
    emaile = pattern.findall(tekst)
    for email in emaile:
        wypisanie(email)


def wypisanie(dopasowanie):
    print(10 * '-')
    print(f'Nazwa: {dopasowanie[0]}')
    print(f'Domena: {dopasowanie[1]}')
    print(f'Rozszeżenie: {dopasowanie[2]}')


if __name__ == "__main__":
    run()
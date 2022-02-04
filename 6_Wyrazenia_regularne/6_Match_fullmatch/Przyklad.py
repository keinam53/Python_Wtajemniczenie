import re


def run():
    numer_txt = "+48 123 456 789 <- to jest numer"
    pattern = re.compile(r"\+(\d{2})((?: \d{3}){3})")
    numer_match = pattern.match(numer_txt)
    #Całe dopasowanie
    print(numer_match.group())
    print(numer_match.group(0))

    #Poszczególne grupy
    print(f'Grupa 1: {numer_match.group(1)}')
    print(f'Grupa 2: {numer_match.group(2)}')

    print(f'Grupa 1: {numer_match[1]}')
    print(f'Grupa 2: {numer_match[2]}')

    for nr_grupy, grupa in enumerate(numer_match.groups()):
        print(f'Grupa {nr_grupy + 1}: {grupa}')

    #Pozycja znalezionych dopasowań
    print(numer_match.start(), numer_match.end())
    print(numer_match.start(1), numer_match.end(1))
    print(numer_match.start(2), numer_match.end(2))


if __name__ == '__main__':
    run()

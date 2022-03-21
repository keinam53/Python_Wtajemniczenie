import re


def run():
    nazwy_plikow = """
rozliczenie.txt
wyniki.txt
wakacje.jpg
pulpit.png
notatka.txt
    """
    pattern = re.compile(r".*.txt")
    print(pattern.finditer(nazwy_plikow))
    for nazwa in pattern.finditer(nazwy_plikow):
        print(nazwa.group())

    numery = "N1: +48 123 456 789, N2: +123 (98)7 654 321, N3: 987 654 321, N4: 987654321"
    pattern_2 = re.compile(r"(?:\+(\d{2,3})[-\s])?\(?(\d{2})\)?(\d[-\s]\d{3}[-\s]\d{3})")
    print(pattern_2.finditer(numery))

    for numer in pattern_2.finditer(numery):
        print(10 * '-')
        print(numer.group())
        for grupa in numer.groups():
            print(grupa)


if __name__ == "__main__":
    run()

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
    print(pattern.findall(nazwy_plikow))

    numery = "N1: +48 123 456 789, N2: +123 (98)7 654 321, N3: 987 654 321, N4: 987654321"
    pattern_2 = re.compile(r"(?:\+(\d{2,3})[-\s])?\(?(\d{2})\)?(\d[-\s]\d{3}[-\s]\d{3})")
    print(pattern_2.findall(numery))

    for numer in pattern_2.findall(numery):
        print(10 * '-')
        for grupa in numer:
            print(grupa)


if __name__ == "__main__":
    run()

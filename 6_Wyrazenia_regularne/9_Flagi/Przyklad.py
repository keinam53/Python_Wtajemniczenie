import re


def run():
    text = "Ala ma kota. Kot nazywa się Mruczek i jest bardzo wesołym zwierzakiem."
    pattern = re.compile(r'kot')
    print(pattern.findall(text))

    pattern_2 = re.compile(r'kot', flags=re.I) #Małe i duże litery
    print(pattern_2.findall(text))


if __name__ == '__main__':
    run()

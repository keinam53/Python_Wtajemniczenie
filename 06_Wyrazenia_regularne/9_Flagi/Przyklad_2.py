import re


def run():
    text = """Ala ma kota. 
Kot nazywa się Mruczek i jest bardzo wesołym zwierzakiem.
Mruczek ma 5 lat."""

    pattern = re.compile(r'^\w+')
    print(pattern.findall(text))

    pattern_2 = re.compile(r'^\w+', flags=re.MULTILINE)
    print(pattern_2.findall(text))

    pattern_3 = re.compile(r'^kot', flags=re.M | re.I)
    print(pattern_3.findall(text))


if __name__ == '__main__':
    run()

import re


def run():
    numer_txt = "+48 123 456 789 <- to jest numer"
    pattern = re.compile(r"\+(\d{2})((?: \d{3}){3})")
    numer_fullmatch = pattern.fullmatch(numer_txt)
    print(numer_fullmatch)

    numer = "+48 123 456 789"
    pattern = re.compile(r"\+(\d{2})((?: \d{3}){3})")
    numer_fullmatch = pattern.fullmatch(numer)
    print(numer_fullmatch.group())


if __name__ == '__main__':
    run()

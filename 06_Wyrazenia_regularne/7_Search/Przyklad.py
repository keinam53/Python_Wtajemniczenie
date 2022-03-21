import re


def run():
    numer_txt = "+48 123 456 789 <- to jest numer"
    pattern = re.compile(r"\+(\d{2})((?: \d{3}){3})")
    numer_search = pattern.search(numer_txt)
    print(numer_search.group())

    numer_txt_2 = "To jest numer -> +48 123 456 789"
    numer_search = pattern.search(numer_txt_2)
    print(numer_search.group())


if __name__ == '__main__':
    run()

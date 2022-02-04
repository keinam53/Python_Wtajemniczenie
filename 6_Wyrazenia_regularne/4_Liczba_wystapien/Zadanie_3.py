import re


def run():
    kody_ok = ["nazwa@domena.com", "nAzWa@dOmEnA.PL"]
    kody_nok = ["nazwa@domenacom", "nazwadomena.com", "nazwa@.com", "@domena.com"]

    pattern = re.compile(r'\w+@\w+\.\w+')

    for kod in kody_ok:
        print(pattern.findall(kod))

    print(10 * '-')
    for kod in kody_nok:
        print(pattern.findall(kod))


if __name__ == '__main__':
    run()

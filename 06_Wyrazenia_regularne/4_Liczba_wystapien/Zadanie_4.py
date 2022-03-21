import re


def run():
    kody_ok = ["https://www.PyJazz.pl", "http://www.pyjazz.com"]
    kody_nok = ["www.pyjazz.pl", "https://www.pyjazz"]

    pattern = re.compile(r'https?://www\.\w+\.\w+')
    for kod in kody_ok:
        print(pattern.findall(kod))

    print(10 * '-')
    for kod in kody_nok:
        print(pattern.findall(kod))


if __name__ == '__main__':
    run()

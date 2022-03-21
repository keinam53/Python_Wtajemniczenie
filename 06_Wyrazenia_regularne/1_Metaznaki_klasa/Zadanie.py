import re


def run():
    kody_ok = ['01-201', '36-065']
    kody_nok = ['1-5494', '536-42', '00a123', 'ac-wgd']

    pattern = re.compile(r'[0-9][0-9]-[0-9][0-9][0-9]')
    for kod in kody_ok:
        print(pattern.findall(kod))

    print(10 * '-')
    for kod in kody_nok:
        print(pattern.findall(kod))


if __name__ == '__main__':
    run()

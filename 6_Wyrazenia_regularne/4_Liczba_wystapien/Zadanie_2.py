import re


def run():
    kody_ok = ['AD-Cq1', 'BG-t8i', 'ABCD2']
    kody_nok = ['1-5494', '536-42', 'a1-ad32', 'ac-wgd']

    pattern = re.compile(r'[A-Z]{2}-?\w{3}')

    for kod in kody_ok:
        print(pattern.findall(kod))

    print(10 * '-')
    for kod in kody_nok:
        print(pattern.findall(kod))


if __name__ == '__main__':
    run()

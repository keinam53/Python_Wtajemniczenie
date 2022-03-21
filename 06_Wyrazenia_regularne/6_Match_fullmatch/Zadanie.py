import re


class AdressError(Exception):
    pass


def run():
    adres = input('Podaj adres e-mail: ')
    pattern = re.compile(r'(\w+)@(\w+)((?:\.\w+)+)')
    adres_fullmatch = pattern.fullmatch(adres)
    if adres_fullmatch is not None:
        print(f'Nazwa: {adres_fullmatch.group(1)}')
        print(f'Domena: {adres_fullmatch.group(2)}')
        print(f'Rozszarzenie domeny: {adres_fullmatch.group(3)}')
    else:
        raise print('Błędna adres')


if __name__ == '__main__':
    run()

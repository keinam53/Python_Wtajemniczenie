def get_email(prefix):
    def generate_email(adress):
        return f'{prefix}-{adress}@{domain}'

    domain = 'domain.com.pl'

    #Inner function jest widoczna w tym miejscu
    admin_email = generate_email('admin')
    info_email = generate_email('info')
    contact_email = generate_email('contact')
    return [admin_email, info_email, contact_email]


def run():
    emails = get_email('mariusz')
    print(emails)


if __name__ == '__main__':
    run()
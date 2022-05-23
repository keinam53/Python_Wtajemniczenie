def anonymize_phone_number(phone_number: str) -> str:
    public_digits_num = 6
    phone_number = phone_number.replace("-", "")
    public_digits = phone_number[:public_digits_num]
    number_of_private_digits = len(phone_number) - public_digits_num
    private_digits = "-" * number_of_private_digits
    return f"{public_digits}{private_digits}"


def test_anonymize_phone_number_replace_digits_after_6_with_hyphens():
    phone_number = "123456789"
    anonymized_phone_number = anonymize_phone_number(phone_number)
    assert anonymized_phone_number == '123456---'

# def test_anonymize_phone_number_replace_digits_after_6_with_hyphens():
#     assert anonymize_phone_number('123456789') == '123456---'


def test_anonymize_phone_number_removes_hyphens_before_anonymization():
    phone_number = "123-456-789"
    anonymized_phone_number = anonymize_phone_number(phone_number)
    assert anonymized_phone_number == '123456---'


def test_anonymize_very_long_phone_number():
    long_phone_number = "123-456-78955565"
    anonymized_phone_number = anonymize_phone_number(long_phone_number)
    assert anonymized_phone_number == '123456--------'

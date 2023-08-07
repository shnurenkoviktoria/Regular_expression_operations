import re
from re_functions import *


def test_find_emails():
    test_text = (
        "Hello, my email is john@example.com. You can also reach me at mary@gmail.com."
    )
    expected_result = ["john@example.com", "mary@gmail.com"]

    assert find_emails(test_text) == expected_result


def test_validate_date():
    assert validate_date("12/11/2023") == True
    assert validate_date("01/01/2023") == True

    assert validate_date("13/31/2023") == False
    assert validate_date("22/30/2023") == False


def test_extract_email_parts():
    email = "john.doe@example.com"
    expected_username = "john.doe"
    expected_domain = "example.com"

    username, domain = extract_email_parts(email)
    assert username == expected_username
    assert domain == expected_domain


def test_validate_phone_number():
    assert validate_phone_number("+1234567890") == True
    assert validate_phone_number("123-456-7890") == True

    assert validate_phone_number("+385(095) 456 789 02") == False
    assert validate_phone_number("+1 123 456 7890 1234") == False


def test_split_sentences():
    text = "Hello! How are you? I hope you are doing well."
    expected_result = ["Hello!", "How are you?", "I hope you are doing well."]

    assert split_sentences(text) == expected_result

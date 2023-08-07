import re


def find_emails(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return re.findall(pattern, text)


def validate_date(date):
    pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$"
    return bool(re.match(pattern, date))


def extract_email_parts(email):
    pattern = (
        r"^(?P<username>[A-Za-z0-9._%+-]+)@(?P<domain>[A-Za-z0-9.-]+\.[A-Za-z]{2,})$"
    )
    match = re.match(pattern, email)
    if match:
        return match.group("username"), match.group("domain")
    else:
        return None, None


def validate_phone_number(phone_number):
    pattern = r"^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    return bool(re.match(pattern, phone_number))


def split_sentences(text):
    pattern = r"(?<=[.!?])\s+"
    return re.split(pattern, text)

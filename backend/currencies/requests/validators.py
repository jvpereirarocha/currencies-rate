from datetime import datetime


def validate_abbreviation_currency(value: str) -> str:
    if len(value) != 3:
        raise ValueError("O campo abreviação deve ter no máximo 3 caracteres")
    if not value.isalpha():
        raise ValueError("O campo abreviação deve ser exclusivamente letras")
    if not value.isupper():
        raise ValueError("O campo abreviação deve ter letras maiúsculas. Ex: USD")

    return value


def validate_date_format(value: str) -> str:
    try:
        datetime.strptime(value, "%d-%m-%Y")
        return value
    except ValueError:
        raise ValueError("O formato da data deve ser YYYY-MM-DD")

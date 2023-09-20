from uuid import uuid4
from pytest import fixture

from domain.entities.currency import Currency, CurrencyRate
from domain.value_objects.currency_date import Date
from domain.value_objects.rate import Rate


@fixture(scope="function")
def mock_currency_rate():
    def _create_mock(
        name: str = "Dollar",
        abbreviation: str = "USD",
        value: float = 1.0,
        date_as_text: str = "01/12/2023",
    ) -> CurrencyRate:
        return CurrencyRate(
            rate_id=uuid4(),
            currency=Currency(
                currency_id=uuid4(),
                name=name,
                abbreviation=abbreviation,
            ),
            rate=Rate(rate_value=value),
            date=Date(date_as_text),
        )

    return _create_mock

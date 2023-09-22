from uuid import uuid4
from pytest import fixture

from domain.entities.currency import Currency


@fixture(scope="function")
def mock_currency():
    def _create_mock(
        name: str = "Dollar",
        abbreviation: str = "USD",
    ) -> Currency:
        return Currency(
            currency_id=uuid4(),
            name=name,
            abbreviation=abbreviation,
        )

    return _create_mock

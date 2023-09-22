from pytest import fixture

from domain.value_objects.currency_date import Date


@fixture(scope="function")
def mock_currency_date():
    def _create_mock(
        day: int = 1,
        month: int = 1,
        year: int = 2021,
    ) -> Date:
        return Date(f"{day}/{month}/{year}")

    return _create_mock

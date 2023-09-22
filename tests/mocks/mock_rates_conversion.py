from uuid import uuid4
from pytest import fixture

from domain.entities.currency import CurrencyRate
from domain.entities.rates_conversion import CurrenciesRatesConversion
from domain.value_objects.interval_of_dates import IntervalOfDates


@fixture(scope="function")
def mock_rates_conversion():
    def _create_mock(
        base_currency_rate: CurrencyRate,
        compare_currency_rate: CurrencyRate,
        interval_of_dates_to_compare: IntervalOfDates,
    ) -> CurrencyRate:
        return CurrenciesRatesConversion(
            currency_rate_id=uuid4(),
            base_currency_rate=base_currency_rate,
            compare_currency_rate=compare_currency_rate,
            interval_of_dates_to_compare=interval_of_dates_to_compare,
        )

    return _create_mock

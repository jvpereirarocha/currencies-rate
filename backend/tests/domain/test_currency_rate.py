from domain.entities.currency import CurrencyRate
from domain.value_objects.interval_of_dates import IntervalOfDates


def test_filter_currency_rate_by_interval(
    mock_currency_rate,
):
    currency_rate_first_day = mock_currency_rate(
        name="Dollar",
        abbreviation="USD",
        value=1.231,
        date_as_text="01/07/2023",
    )
    currency_rate_second_day = mock_currency_rate(
        name="Dollar",
        abbreviation="USD",
        value=1.445,
        date_as_text="02/07/2023",
    )
    currency_rate_third_day = mock_currency_rate(
        name="Dollar",
        abbreviation="USD",
        value=1.825,
        date_as_text="03/07/2023",
    )
    currency_rate_last_day = mock_currency_rate(
        name="Dollar",
        abbreviation="USD",
        value=2.751,
        date_as_text="04/07/2023",
    )

    all_currency_rates = [
        currency_rate_first_day,
        currency_rate_second_day,
        currency_rate_third_day,
        currency_rate_last_day,
    ]

    interval_of_dates = IntervalOfDates(
        start_date=currency_rate_first_day.date,
        end_date=currency_rate_third_day.date,
    )

    filtered_currencies_rates = list(
        CurrencyRate.filter_currencies_rates_by_interval(
            currencies_rates=all_currency_rates,
            interval_of_dates=interval_of_dates,
        )
    )

    assert len(filtered_currencies_rates) == 3

    assert filtered_currencies_rates == [
        currency_rate_first_day,
        currency_rate_second_day,
        currency_rate_third_day,
    ]

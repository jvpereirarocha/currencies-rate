from pytest import mark
from domain.value_objects.currency_date import Date

from domain.value_objects.interval_of_dates import IntervalOfDates


@mark.parametrize(
    "interval_of_dates, interval_length_in_days, interval_is_valid",
    [
        (
            IntervalOfDates(
                start_date=Date("01/09/2023"),
                end_date=Date("08/09/2023"),
            ),
            5,
            True,
        ),
        (
            IntervalOfDates(
                start_date=Date("06/09/2023"),
                end_date=Date("11/09/2023"),
            ),
            3,
            True,
        ),
        (
            IntervalOfDates(
                start_date=Date("16/09/2023"),
                end_date=Date("25/09/2023"),
            ),
            7,
            True,
        ),
        (
            IntervalOfDates(
                start_date=Date("11/09/2023"),
                end_date=Date("16/09/2023"),
            ),
            5,
            False,
        ),
    ],
)
def test_interval_of_dates_is_valid(
    interval_of_dates: IntervalOfDates,
    interval_length_in_days: int,
    interval_is_valid: bool,
) -> None:
    assert (
        interval_of_dates.interval_of_dates_is_valid(
            interval_length_in_days=interval_length_in_days
        )
        == interval_is_valid
    )

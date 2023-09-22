from dataclasses import dataclass
from typing import List, TYPE_CHECKING
from uuid import UUID, uuid4
from domain.entities.base_currency import Entity

from domain.value_objects.currency_date import Date
from domain.value_objects.rate import Rate


if TYPE_CHECKING:
    from domain.value_objects.interval_of_dates import IntervalOfDates


@dataclass()
class Currency(Entity):
    currency_id: UUID
    name: str
    abbreviation: str


@dataclass()
class CurrencyRate(Entity):
    rate_id: UUID
    currency: Currency
    rate: Rate
    date: Date

    def __eq__(self, other: "CurrencyRate") -> bool:
        return (
            self.rate_id == other.rate_id
            and self.currency == other.currency
            and self.rate == other.rate
            and self.date == other.date
        )

    def __hash__(self) -> int:
        return hash(self.rate_id)

    @classmethod
    def new_currency_rate(
        cls,
        name: str,
        abbreviation: str,
        rate_value: float,
        date_as_string: str,
    ) -> "CurrencyRate":
        return cls(
            rate_id=uuid4(),
            currency=Currency(
                currency_id=uuid4(),
                name=name,
                abbreviation=abbreviation,
            ),
            rate=Rate(rate_value),
            date=Date(date_as_string),
        )

    @classmethod
    def filter_currencies_rates_by_interval(
        cls,
        currencies_rates: List["CurrencyRate"],
        interval_of_dates: "IntervalOfDates",
    ) -> List["CurrencyRate"]:
        for currency_rate in currencies_rates:
            if interval_of_dates.date_is_in_the_interval(
                date_to_compare=currency_rate.date
            ):
                yield currency_rate

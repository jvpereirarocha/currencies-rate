from dataclasses import dataclass
from uuid import UUID
from domain.entities.base_currency import Entity

from domain.entities.currency import CurrencyRate
from domain.value_objects.interval_of_dates import IntervalOfDates


@dataclass()
class CurrenciesRatesConversion(Entity):
    """
    This entity represents a conversion between two currencies rates
    """

    currency_rate_id: UUID
    base_currency_rate: CurrencyRate
    compare_currency_rate: CurrencyRate
    interval_of_dates_to_compare: IntervalOfDates

    def __hash__(self) -> int:
        return hash(self.currency_rate_id)

    def __eq__(self, other: "CurrenciesRatesConversion") -> bool:
        return self.currency_rate_id == other.currency_rate_id

    def __ne__(self, other: "CurrenciesRatesConversion") -> bool:
        return not self.__eq__(other)

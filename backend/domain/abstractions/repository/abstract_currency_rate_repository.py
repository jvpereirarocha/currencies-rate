from abc import ABC, abstractmethod
from datetime import date
from typing import Optional, Set

from domain.entities.currency import CurrencyRate
from domain.abstractions.repository.abstract_repo import AbstractRepository


class AbstractCurrencyRateRepository(AbstractRepository):
    @abstractmethod
    def get_currency_rate_by_name_abbreviation_and_date(
        self, currency: str, date: date
    ) -> Optional[CurrencyRate]:
        raise NotImplementedError()

    @abstractmethod
    def save_currency_rate(self, currency_rate: CurrencyRate) -> None:
        raise NotImplementedError()

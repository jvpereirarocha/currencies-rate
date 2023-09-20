from abc import ABC, abstractmethod
from typing import Set

from domain.entities.currency import CurrencyRate
from domain.abstractions.repository.abstract_repo import AbstractRepository


class AbstractCurrencyRateRepository(AbstractRepository):
    def __init__(
        self,
    ):
        self._entities: Set[CurrencyRate] = set()

    @abstractmethod
    def get_currency_rate_by_name_abbreviation_and_date(
        self, currency: str
    ) -> CurrencyRate:
        raise NotImplementedError()

    @abstractmethod
    def save_currency_rate(self, currency_rate: CurrencyRate) -> None:
        raise NotImplementedError()

    def commit(self):
        pass
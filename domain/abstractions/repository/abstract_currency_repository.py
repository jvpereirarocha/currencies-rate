from abc import ABC, abstractmethod
from datetime import date
from typing import List

from domain.entities.currency import Currency
from domain.abstractions.repository.abstract_repo import AbstractRepository


class AbstractCurrencyRepository(AbstractRepository):
    @abstractmethod
    def get_currency_by_name_and_abbreviation(
        self, name: str, abbreviation: str
    ) -> Currency:
        raise NotImplementedError()

    @abstractmethod
    def save_currency(self, name: str, abbreviation: str) -> Currency:
        raise NotImplementedError()

    @abstractmethod
    def get_all_currencies(self) -> List[Currency]:
        raise NotImplementedError()

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError()

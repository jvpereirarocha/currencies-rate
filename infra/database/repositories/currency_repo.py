from datetime import date
from typing import List, Optional, Set, TYPE_CHECKING
from domain.abstractions.repository.abstract_currency_repository import (
    AbstractCurrencyRepository,
)
from domain.entities.currency import Currency as CurrencyEntity, Currency
from currencies.models import Currency as CurrencyORM

if TYPE_CHECKING:
    from django.db.models import Model


class CurrencyRepo(AbstractCurrencyRepository):
    def __init__(self) -> None:
        self._entities_to_commit: Set[Model] = set()

    def _filter_currency_by_abbreviation_and_name(
        self, abbreviation: str, name: str
    ) -> bool:
        return CurrencyORM.objects.filter(
            abbreviation__iexact=abbreviation, name__iexact=name
        ).exists()

    def get_all_currencies(self) -> List[CurrencyEntity]:
        return [
            CurrencyEntity(
                currency_id=currency.currency_id,
                name=currency.name,
                abbreviation=currency.abbreviation,
            )
            for currency in CurrencyORM.objects.all()
        ]

    def get_currency_by_name_and_abbreviation(
        self, name: str, abbreviation: str
    ) -> CurrencyEntity:
        query = CurrencyORM.objects.filter(name=name, abbreviation=abbreviation).first()
        if query is None:
            return

        return CurrencyEntity(
            currency_id=query.currency_id,
            name=query.name,
            abbreviation=query.abbreviation,
        )

    def save_currency(self, name: str, abbreviation: str) -> CurrencyEntity:
        currency_already_exists = self._filter_currency_by_abbreviation_and_name(
            abbreviation=abbreviation, name=name
        )
        if currency_already_exists:
            entity = CurrencyORM(
                currency_id=CurrencyEntity.generate_uuid(),
                name=name,
                abbreviation=abbreviation,
            )
            self._entities_to_commit.add(entity)

            return CurrencyEntity(
                currency_id=entity.currency_id,
                name=entity.name,
                abbreviation=entity.abbreviation,
            )

    def commit(self) -> None:
        for entity in self._entities_to_commit:
            entity.save()

        self._entities_to_commit.clear()

    def rollback(self) -> None:
        self._entities_to_commit.clear()

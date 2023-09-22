from datetime import date
from typing import Optional, Set, TYPE_CHECKING
from domain.abstractions.repository.abstract_currency_rate_repository import (
    AbstractCurrencyRateRepository,
)
from domain.entities.currency import CurrencyRate as CurrencyRateEntity
from domain.entities.currency import Currency as CurrencyEntity
from currencies.models import CurrencyRate as CurrencyRateORM
from currencies.models import Currency as CurrencyORM
from domain.value_objects.currency_date import Date
from domain.value_objects.rate import Rate

if TYPE_CHECKING:
    from django.db.models import Model


class CurrencyRateRepo(AbstractCurrencyRateRepository):
    def __init__(self) -> None:
        self._entities_to_commit: Set[Model] = set()

    def _filter_currency_by_abbreviation_name(
        self, currency: str
    ) -> Optional[CurrencyORM]:
        return CurrencyORM.objects.filter(abbreviation__iexact=currency).first()

    def get_currency_rate_by_name_abbreviation_and_date(
        self, currency: str, date: date
    ) -> Optional[CurrencyRateEntity]:
        orm_currency = self._filter_currency_by_abbreviation_name(currency)
        if orm_currency is None:
            return

        orm_currency_rate = CurrencyRateORM.objects.filter(
            currency_id=orm_currency.currency_id, date=date
        ).first()
        if orm_currency_rate is None:
            return

        return CurrencyRateEntity(
            rate_id=orm_currency_rate.currency_rate_id,
            currency=CurrencyEntity(
                currency_id=orm_currency.currency_id,
                name=orm_currency.name,
                abbreviation=orm_currency.abbreviation,
            ),
            rate=Rate(orm_currency_rate.rate),
            date=Date(orm_currency_rate.date.strftime("%d/%m/%Y")),
        )

    def save_currency_rate(self, currency_rate: CurrencyRateEntity) -> None:
        currency_orm = CurrencyORM(
            currency_id=currency_rate.currency.currency_id,
            name=currency_rate.currency.name,
            abbreviation=currency_rate.currency.abbreviation,
        )
        currency_rate_orm = CurrencyRateORM(
            currency_rate_id=currency_rate.rate_id,
            currency=currency_orm.currency_id,
            rate=currency_rate.rate.value,
            date=date(
                year=currency_rate.date.year,
                month=currency_rate.date.month,
                day=currency_rate.date.day,
            ),
        )
        self._entities_to_commit.add(currency_orm)
        self._entities_to_commit.add(currency_rate_orm)

    def commit(self) -> None:
        for entity in self._entities_to_commit:
            entity.save()

        self._entities_to_commit.clear()

    def rollback(self) -> None:
        self._entities_to_commit.clear()

from datetime import date
from typing import Optional, Set
from domain.abstractions.repository.abstract_currency_rate_repository import (
    AbstractCurrencyRateRepository
)
from domain.entities.currency import CurrencyRate as CurrencyRateEntity
from domain.entities.currency import Currency as CurrencyEntity
from currencies.models import CurrencyRate as CurrencyRateORM
from currencies.models import Currency as CurrencyORM
from domain.value_objects.currency_date import Date
from domain.value_objects.rate import Rate


class CurrencyRateRepo(AbstractCurrencyRateRepository):

    def _filter_currency_by_abbrevation_name(self, currency: str) -> Optional[CurrencyORM]:
        return CurrencyORM.objects.filter(abbreviation__iexact=currency).first()

    def get_currency_rate_by_name_abbreviation_and_date(
        self, currency: str, date: date
    ) -> Optional[CurrencyRateEntity]:
        
        orm_currency = self._filter_currency_by_abbrevation_name(currency)
        if orm_currency is None:
            return
        
        orm_currency_rate = CurrencyRateORM.objects.filter(
            currency_id=orm_currency.currency_id,
            date=date
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
        CurrencyRateORM.objects.create(
            currency_rate_id=currency_rate.rate_id,
            currency_id=currency_rate.currency.currency_id,
            rate=currency_rate.rate.value,
            date=currency_rate.date.value,
        )
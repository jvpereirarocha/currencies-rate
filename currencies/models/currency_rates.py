from django.db import models
from currencies.models.currency import Currency


class CurrencyRateValidators:
    class InvalidCurrencyRateValue(Exception):
        pass

    @staticmethod
    def validate_currency_rate_value(rate_value: float) -> None:
        if rate_value < 0:
            raise CurrencyRateValidators.InvalidCurrencyRateValue()


class CurrencyRate(models.Model):
    currency_rate_id = models.UUIDField(primary_key=True)
    currency = models.ForeignKey(
        Currency, related_name="currency", on_delete=models.CASCADE, db_index=True
    )
    rate = models.FloatField(
        db_index=True,
        null=False,
        blank=False,
        validators=[CurrencyRateValidators.validate_currency_rate_value],
    )
    date = models.DateField(db_index=True, null=False, blank=False)

    class Meta:
        db_table = "currency_rates"
        unique_together = ("currency_rate_id", "currency", "date")

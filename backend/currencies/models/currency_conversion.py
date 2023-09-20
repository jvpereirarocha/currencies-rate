from django.db import models
from currencies.models.currency_rates import CurrencyRate


class CurrencyConversion(models.Model):
    currency_conversion_id = models.UUIDField(primary_key=True)
    base_currency_rate = models.ForeignKey(
        CurrencyRate,
        related_name="base_currency_rate",
        on_delete=models.CASCADE,
        db_index=True,
    )
    compare_currency_rate = models.ForeignKey(
        CurrencyRate,
        related_name="compare_currency_rate",
        on_delete=models.CASCADE,
        db_index=True,
    )
    start_date = models.DateField(db_index=True, null=False, blank=False)
    end_date = models.DateField(db_index=True, null=False, blank=False)

    class Meta:
        db_table = "currencies_conversion"

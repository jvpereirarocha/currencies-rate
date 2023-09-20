from django.db import models


class CurrencyValidators:
    class InvalidCurrencyAbbreviation(Exception):
        pass

    @staticmethod
    def validate_abbreviation_uppercase(abbreviation: str) -> None:
        if not abbreviation.isupper():
            raise CurrencyValidators.InvalidCurrencyAbbreviation()


class Currency(models.Model):
    _validators = CurrencyValidators

    currency_id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255, db_index=True, null=False)
    abbreviation = models.CharField(
        max_length=5,
        db_index=True,
        null=False,
        validators=[_validators.validate_abbreviation_uppercase],
    )

    class Meta:
        db_table = "currencies"

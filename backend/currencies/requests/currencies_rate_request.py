from pydantic import BaseModel
from domain.abstractions.requests.abstract_request import AbstractRequest
from typing_extensions import Annotated
from pydantic import BaseModel, Field, field_validator
from currencies.requests import validators


class CurrenciesRateModel(BaseModel):
    start_date: str = Annotated[str, Field(max_length=10, validate_default=True)]
    end_date: str = Annotated[str, Field(max_length=10, validate_default=True)]
    from_base_currency: str = Annotated[str, Field(max_length=3, validate_default=True)]
    to_compare_currency: str = Annotated[
        str, Field(max_length=3, validate_default=True)
    ]

    @field_validator("from_base_currency", "to_compare_currency")
    def validate_currency(cls, value: str) -> str:
        return validators.validate_abbreviation_currency(value)

    @field_validator("start_date", "end_date")
    def validate_date(cls, value: str) -> str:
        return validators.validate_date_format(value)


class CurrenciesRateRequest(AbstractRequest):
    def __init__(self, **kwargs) -> None:
        self.start_date = kwargs.get("start_date")
        self.end_date = kwargs.get("end_date")
        self.from_base_currency = kwargs.get("from_base_currency")
        self.to_compare_currency = kwargs.get("to_compare_currency")
        self.validate()

    def _validate_attributes(self) -> None:
        if not self.start_date:
            raise Exception("O campo data inicial é obrigatório")
        if not self.end_date:
            raise Exception("O campo data final é obrigatório")
        if not self.from_base_currency:
            raise Exception("O campo moeda base é obrigatório")
        if not self.to_compare_currency:
            raise Exception("O campo moeda de comparação é obrigatório")

    def validate(self) -> None:
        try:
            self._validate_attributes()
            CurrenciesRateModel(
                start_date=self.start_date,
                end_date=self.end_date,
                from_base_currency=self.from_base_currency,
                to_compare_currency=self.to_compare_currency,
            )
        except Exception as error:
            raise Exception(error)

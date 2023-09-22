from currencies.requests import validators
from domain.abstractions.requests.abstract_request import AbstractRequest

from typing_extensions import Annotated
from pydantic import BaseModel, Field, field_validator


class CurrencyModel(BaseModel):
    name: str = Annotated[str, Field(max_length=50, validate_default=True)]
    abbreviation: str = Annotated[str, Field(max_length=3, validate_default=True)]

    @field_validator("abbreviation")
    def validate_abbreviation(cls, value: str) -> str:
        return validators.validate_abbreviation_currency(value)


class CurrencyRequest(AbstractRequest):
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get("name")
        self.abbreviation = kwargs.get("abbreviation")
        self.validate()

    def _validate_attributes(self) -> None:
        if not self.name:
            raise Exception("O campo nome é obrigatório")
        if not self.abbreviation:
            raise Exception("O campo abreviação é obrigatório")

    def validate(self) -> None:
        try:
            self._validate_attributes()
            CurrencyModel(name=self.name, abbreviation=self.abbreviation)
        except Exception as error:
            raise Exception(error)


class GetAllCurrenciesRequest(AbstractRequest):
    def __init__(self, **kwargs) -> None:
        self.validate()

    def validate(self) -> None:
        pass

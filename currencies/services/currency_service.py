from domain.abstractions.repository.abstract_repo import AbstractRepository
from domain.value_objects.base_response_data_structure import ResponseData
from domain.entities.currency import Currency
from domain.abstractions.services.abstract_services import AbstractService
from domain.abstractions.repository.abstract_currency_repository import (
    AbstractCurrencyRepository,
)
from domain.abstractions.requests.abstract_request import AbstractRequest


class CurrencyService(AbstractService):
    """
    Service for currencies.
    """

    def __init__(
        self, request: AbstractRequest, repo: AbstractCurrencyRepository
    ) -> None:
        super().__init__(request, repo)
        self.data = None
        self.status_code = None

    def __check_if_currency_exists(self, name: str, abbreviation: str) -> bool:
        """
        Checks if currency exists.
        """
        return (
            self.repo.get_currency_by_name_and_abbreviation(
                name=name, abbreviation=abbreviation
            )
            is not None
        )

    def register_new_currency(self) -> Currency:
        """
        Creates a currency.
        """
        currency_already_exists = self.__check_if_currency_exists(
            name=self.request.name, abbreviation=self.request.abbreviation
        )
        if currency_already_exists:
            raise Exception("Currency already exists.")

        self.repo.save_currency(
            name=self.request.name, abbreviation=self.request.abbreviation
        )
        self.data = {
            "currency_name": self.request.name,
            "currency_abbreviation": self.request.abbreviation,
        }
        self.status_code = 201
        self.repo.commit()

    def make_response(self) -> ResponseData:
        return ResponseData(
            type_of_response="success",
            message=self.data,
            status_code=self.status_code,
        )


class GetAllCurrenciesService(AbstractService):
    def __init__(
        self, request: AbstractRequest, repo: AbstractCurrencyRepository
    ) -> None:
        super().__init__(request, repo)
        self.data = None
        self.status_code = None

    def get_all(self) -> None:
        """
        Gets all currencies.
        """
        all_currencies = self.repo.get_all_currencies()
        self.data = [
            {
                "currency_name": currency.name,
                "currency_abbreviation": currency.abbreviation,
            }
            for currency in all_currencies
        ]
        self.status_code = 200

    def make_response(self) -> ResponseData:
        return ResponseData(
            type_of_response="success",
            message=self.data,
            status_code=self.status_code,
        )

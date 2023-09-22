from domain.abstractions.repository.abstract_currency_rate_repository import (
    AbstractCurrencyRateRepository,
)
from domain.abstractions.requests.abstract_request import AbstractRequest
from domain.abstractions.services.abstract_services import AbstractService
from domain.value_objects.base_response_data_structure import ResponseData
from domain.value_objects.currency_date import Date
from domain.value_objects.interval_of_dates import IntervalOfDates
from currencies.services.currency_vat_api_service import VatCurrenciesRateAPIService


class CurrenciesRateService(AbstractService):
    def __init__(
        self, request: AbstractRequest, repo: AbstractCurrencyRateRepository
    ) -> None:
        super().__init__(request, repo)
        self.data = None
        self.status_code = None
        self.error = None

    @property
    def interval_is_valid(self) -> bool:
        return self._check_if_interval_is_valid()

    @property
    def currencies_are_the_same(self) -> bool:
        return self._validate_if_currencies_are_the_same()

    @classmethod
    def format_date_to_brazilian_date_format(cls, date_to_format: str) -> str:
        try:
            day, month, year = date_to_format.split("-")
            return f"{day}/{month}/{year}"
        except Exception as e:
            raise Exception(e)

    @classmethod
    def format_date_to_api_date_format(cls, date_to_format: str) -> str:
        try:
            day, month, year = date_to_format.split("-")
            return f"{year}-{month}-{day}"
        except Exception as e:
            raise Exception(e)

    def _check_if_interval_is_valid(self) -> bool:
        start_date = self.format_date_to_brazilian_date_format(self.request.start_date)
        end_date = self.format_date_to_brazilian_date_format(self.request.end_date)
        interval_of_dates = IntervalOfDates(
            start_date=Date(start_date),
            end_date=Date(end_date),
        )
        return interval_of_dates.interval_of_dates_is_valid(interval_length_in_days=7)

    def _validate_if_currencies_are_the_same(self) -> bool:
        return self.request.from_base_currency == self.request.to_compare_currency

    def get_data_from_api(self) -> None:
        api_service = VatCurrenciesRateAPIService(
            query_params={
                "base": self.request.from_base_currency,
                "date": self.format_date_to_api_date_format(self.request.start_date),
            }
        )
        self.data, self.status_code = api_service.make_api_call()

    def get_currencies_rate(self) -> None:
        self.get_data_from_api()

    def make_response(self) -> ResponseData:
        type_of_response = "success"
        if not self.interval_is_valid:
            type_of_response = "error"
            self.error = "O intervalo é inválido"
            self.status_code = 400

        if self.currencies_are_the_same:
            type_of_response = "error"
            self.error = "Não é possível comparar a mesma moeda"
            self.status_code = 400

        if self.error:
            return ResponseData(
                type_of_response=type_of_response,
                message=self.error,
                status_code=self.status_code,
            )

        return ResponseData(
            type_of_response=type_of_response,
            message=self.data,
            status_code=self.status_code,
        )

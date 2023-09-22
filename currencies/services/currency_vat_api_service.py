from typing import Dict, List, Tuple
from currencies.mixins import APIMixin
from domain.abstractions.services.abstract_services import AbstractExternalAPIService
from domain.value_objects.vat_comply_endpoints import (
    BASE_API_VAT_COMPLY_URL,
    CURRENCIES_RATE_ENDPOINT,
)


class VatCurrenciesRateAPIService(AbstractExternalAPIService, APIMixin):
    def __init__(self, query_params: Dict[str, str] = {}) -> None:
        super().__init__(query_params)
        self.status_code = None
        self.data = None

    def mount_query_params(self) -> str:
        complete_query_params = ""
        for index, (key, value) in enumerate(self.query_params.items()):
            if index == 0 and len(self.query_params) == 1:
                complete_query_params += f"?{key}={value}"
            elif index == 0 and len(self.query_params) > 1:
                complete_query_params += f"?{key}={value}&"

            elif index == len(self.query_params) - 1:
                complete_query_params += f"{key}={value}"

            else:
                complete_query_params += f"{key}={value}&"

        return complete_query_params

    def get_from_base_to_compare_currency_rate(self) -> Dict[str, str]:
        try:
            query_params = self.mount_query_params()
            url = f"{BASE_API_VAT_COMPLY_URL}/{CURRENCIES_RATE_ENDPOINT}{query_params}"
            response = self.get(url=url, query_params=self.query_params)
            return {
                "from_base_currency": response["base"],
                "to_compare_currencies": response["rates"],
            }
        except Exception as e:
            return {"error": e}

    def make_api_call(self) -> Tuple[dict, int]:
        self.data = self.get_from_base_to_compare_currency_rate()
        self.status_code = 200
        return self.data, self.status_code

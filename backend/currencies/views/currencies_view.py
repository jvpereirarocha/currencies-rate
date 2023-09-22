from django.http import HttpResponse
from domain.value_objects.base_response_data_structure import ResponseData
from currencies.services.currency_service import CurrencyService
from currencies.dependency_injection import DependencyInjection
from currencies.requests.currency_request import CurrencyRequest
from infra.database.repositories.currency_repo import CurrencyRepo
from currencies.responses import Response
import json


@DependencyInjection(
    input_request=CurrencyRequest, repository=CurrencyRepo, response=Response
)
def get_all_currencies(request):
    pass


@DependencyInjection(
    input_request=CurrencyRequest, repository=CurrencyRepo, response=Response
)
def register_new_currency(request):
    request_data = json.loads(request.body)
    data = CurrencyRequest(
        name=request_data["currencyName"],
        abbreviation=request_data["currencyAbbreviation"],
    )
    repository = CurrencyRepo()
    currency_service = CurrencyService(request=data, repo=repository)
    currency_service.register_new_currency()
    service_response: ResponseData = currency_service.make_response()
    response, status_code = Response(response_data=service_response).build_response()
    http_response = HttpResponse(response, content_type="application/json")
    http_response.status_code = status_code
    return http_response
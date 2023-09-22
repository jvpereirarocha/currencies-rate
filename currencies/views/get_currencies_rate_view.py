from django.http import HttpResponse
from currencies.dependency_injection import DependencyInjection
from currencies.requests.currencies_rate_request import CurrenciesRateRequest
from currencies.responses import Response
from currencies.services.currencies_rate_service import CurrenciesRateService
from infra.database.repositories.currency_rate_repo import CurrencyRateRepo


@DependencyInjection(
    input_request=CurrenciesRateRequest, repository=CurrencyRateRepo, response=Response
)
def get_currencies_rate_view(request):
    query_params = request.GET
    repository = CurrencyRateRepo()
    request_currencies_rate = CurrenciesRateRequest(
        from_base_currency=query_params.get("fromBase"),
        to_compare_currency=query_params.get("toCompare"),
        start_date=query_params.get("startDate"),
        end_date=query_params.get("endDate"),
    )
    service = CurrenciesRateService(request=request_currencies_rate, repo=repository)
    service.get_currencies_rate()
    service_response = service.make_response()
    response, status_code = Response(response_data=service_response).build_response()
    http_response = HttpResponse(response, content_type="application/json")
    http_response.status_code = status_code
    return http_response

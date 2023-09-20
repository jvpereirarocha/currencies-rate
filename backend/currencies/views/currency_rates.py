from django.http import HttpResponse
from currencies.dependency_injection import DependencyInjection


@DependencyInjection(
    input_request="request",
    repository="repository",
    response="response"
)
def get_currencies_rates(request):
    return HttpResponse("Hello, world. You're at the currencies index.")

from django.http import HttpResponse


def get_currencies_rates(request):
    return HttpResponse("Hello, world. You're at the currencies index.")
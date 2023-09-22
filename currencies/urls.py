"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from currencies.views.index import index
from currencies.views.currencies_view import register_new_currency, get_all_currencies
from currencies.views.get_currencies_rate_view import get_currencies_rate_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", index, name="index"),
    path("get_all/", get_all_currencies, name="get_all_currencies"),
    path(
        "register_new_currency/",
        csrf_exempt(register_new_currency),
        name="register_new_currency",
    ),
    path("get_currencies_rate/", get_currencies_rate_view, name="get_currencies_rate"),
]

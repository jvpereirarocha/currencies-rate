from typing import Dict
import requests


class APIMixin:
    def post(self, url: str, data: dict) -> dict:
        response = requests.post(url, data=data)
        return response.json()

    def get(self, url: str, query_params: Dict[str, str]) -> dict:
        response = requests.get(url, params=query_params)
        return response.json()

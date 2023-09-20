from typing import Any
from domain.abstractions.requests.abstract_request import AbstractRequest
from domain.abstractions.repository.abstract_repo import AbstractRepository
from domain.abstractions.responses.abstract_response import AbstractResponse


class DependencyInjection:

    def __init__(self, input_request: str = None, repository: str = None, response: str = None) -> None:
        self.request = input_request
        self.repository = repository
        self.response = response

    def _validate_request_instance(self):
        if isinstance(self.request, AbstractRequest) is False:
            raise Exception("Request instance is invalid")
        
    def _validate_repository_instance(self):
        if isinstance(self.repository, AbstractRepository) is False:
            raise Exception("Repository instance is invalid")

    def _validate_response_instance(self):
        if isinstance(self.response, AbstractResponse) is False:
            raise Exception("Response instance is invalid")

    def _validate_instances(self):
        if not self.repository or not self.request or not self.response:
            raise Exception("Request, Repository and Response are required")
        
        self._validate_request_instance()
        self._validate_repository_instance()
        self._validate_response_instance()

    def __call__(self, func: callable) -> Any:
        self._validate_instances()
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
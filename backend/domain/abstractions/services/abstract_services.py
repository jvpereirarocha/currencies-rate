from abc import ABC, abstractmethod
from domain.abstractions.repository.abstract_repo import AbstractRepository

from domain.abstractions.requests.abstract_request import AbstractRequest
from domain.value_objects.base_response_data_structure import ResponseData


class AbstractService(ABC):
    def __init__(self, request: AbstractRequest, repo: AbstractRepository) -> None:
        self.request = request
        self.repo = repo
        self.__validate()

    """
    Base class for services.
    """

    def __validate(self) -> None:
        """
        Validates the request.
        """
        if not self.request or not self.repo:
            raise Exception("Invalid request or repository.")

    @abstractmethod
    def make_response(self) -> ResponseData:
        """
        Makes a response.
        """
        raise NotImplementedError()

from abc import ABC
from domain.abstractions.repository.abstract_repo import AbstractRepository

from domain.abstractions.requests.abstract_request import AbstractRequest


class AbstractService(ABC):
    def __init__(self, request: AbstractRequest, repo: AbstractRepository) -> None:
        self.request = request
        self.repo = repo
    
    """
    Base class for services.
    """
    pass
from abc import ABC, abstractmethod


class AbstractResponse(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def build_response(self, data: dict = None) -> dict:
        raise NotImplementedError()
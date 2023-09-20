from abc import ABC, abstractmethod


class AbstractRequest(ABC):
    def __init__(self) -> None:
        self.validate()

    @abstractmethod
    def validate(self) -> None:
        """
        Validate request.
        """
        raise NotImplementedError()
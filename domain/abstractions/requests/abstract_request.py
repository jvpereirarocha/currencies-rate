from abc import ABC, abstractmethod


class AbstractRequest(ABC):
    @abstractmethod
    def validate(self) -> None:
        """
        Validate request.
        """
        raise NotImplementedError()

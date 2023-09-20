from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    """
    Base class for repositories.
    """

    @abstractmethod
    def commit(self):
        """
        Commit changes to the repository.
        """
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        """
        Rollback changes to the repository.
        """
        raise NotImplementedError()

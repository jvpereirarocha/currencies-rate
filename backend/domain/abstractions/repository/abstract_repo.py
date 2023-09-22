from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    """
    Base class for repositories.
    """

    @abstractmethod
    def commit(self):
        """
        Commit changes.
        """
        pass

    @abstractmethod
    def rollback(self):
        """
        Rollback changes.
        """
        pass

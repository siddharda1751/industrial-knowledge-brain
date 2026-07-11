from abc import ABC, abstractmethod

from app.online.models import GraphResult, Query


class BaseGraphRetriever(ABC):

    @abstractmethod
    def search(
        self,
        query: Query
    ) -> GraphResult:
        """
        Perform graph traversal.
        """
        pass
from abc import ABC, abstractmethod

from app.online.models import Query, RetrievedChunk


class BaseBM25Retriever(ABC):

    @abstractmethod
    def search(
        self,
        query: Query
    ) -> list[RetrievedChunk]:
        """
        Perform keyword search.
        """
        pass
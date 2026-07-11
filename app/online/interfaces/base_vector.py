from abc import ABC, abstractmethod

from app.online.models import Query, RetrievedChunk


class BaseVectorRetriever(ABC):

    @abstractmethod
    def search(
        self,
        query: Query
    ) -> list[RetrievedChunk]:
        """
        Perform semantic search using vector embeddings.
        """
        pass
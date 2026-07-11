from abc import ABC, abstractmethod

from app.online.models import DocumentChunk


class BaseDocumentStore(ABC):

    @abstractmethod
    def fetch(
        self,
        chunk_ids: list[str]
    ) -> list[DocumentChunk]:
        """
        Fetch original document chunks.
        """
        pass
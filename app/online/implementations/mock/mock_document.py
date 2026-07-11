from app.online.implementations.mock.mock_data import MOCK_DOCUMENTS
from app.online.interfaces.base_document_store import BaseDocumentStore
from app.online.models import DocumentChunk


class MockDocumentStore(BaseDocumentStore):

    def fetch(
        self,
        chunk_ids: list[str]
    ) -> list[DocumentChunk]:

        documents = []

        for chunk_id in chunk_ids:

            if chunk_id in MOCK_DOCUMENTS:
                documents.append(
                    MOCK_DOCUMENTS[chunk_id]
                )

        return documents
from app.online.implementations.mock.mock_data import MOCK_RETRIEVAL_RESULTS
from app.online.interfaces.base_vector import BaseVectorRetriever
from app.online.models import Query, RetrievedChunk


class MockVectorRetriever(BaseVectorRetriever):

    def search(
        self,
        query: Query
    ) -> list[RetrievedChunk]:

        results = []

        query_text = query.query.lower()

        for chunk in MOCK_RETRIEVAL_RESULTS.values():

            summary = (
                chunk.text_summary +
                " " +
                chunk.table_summary +
                " " +
                chunk.image_summary
            ).lower()

            if any(
                word in summary
                for word in query_text.split()
            ):
                results.append(chunk)

        return results
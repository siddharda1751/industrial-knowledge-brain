from app.online.implementations.mock.mock_data import (
    MOCK_KEYWORDS,
    MOCK_RETRIEVAL_RESULTS,
)
from app.online.interfaces.base_bm25 import BaseBM25Retriever
from app.online.models import (
    Query,
    RetrievedChunk,
    RetrievalSource,
)


class MockBM25Retriever(BaseBM25Retriever):

    def search(
        self,
        query: Query
    ) -> list[RetrievedChunk]:

        results = {}

        query_text = query.query.lower()

        for keyword, chunk_ids in MOCK_KEYWORDS.items():

            if keyword in query_text:

                for chunk_id in chunk_ids:

                    if chunk_id in MOCK_RETRIEVAL_RESULTS:

                        chunk = MOCK_RETRIEVAL_RESULTS[
                            chunk_id
                        ].model_copy(
                            update={
                                "score": 1.0,
                                "source": RetrievalSource.BM25
                            }
                        )

                        results[chunk.chunk_id] = chunk

        return list(results.values())
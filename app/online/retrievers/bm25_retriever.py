from app.online.interfaces.base_bm25 import BaseBM25Retriever
from app.online.models import Query, RetrievedChunk


class BM25Retriever:

    def __init__(
        self,
        bm25_store: BaseBM25Retriever
    ):
        self.bm25_store = bm25_store

    def retrieve(
        self,
        query: Query
    ) -> list[RetrievedChunk]:

        return self.bm25_store.search(query)
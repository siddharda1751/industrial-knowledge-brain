from app.online.models import RetrievalResult, Query

from .bm25_retriever import BM25Retriever
from .graph_retriever import GraphRetriever
from .vector_retriever import VectorRetriever


class HybridRetriever:

    def __init__(
        self,
        vector_retriever: VectorRetriever,
        bm25_retriever: BM25Retriever,
        graph_retriever: GraphRetriever
    ):

        self.vector_retriever = vector_retriever

        self.bm25_retriever = bm25_retriever

        self.graph_retriever = graph_retriever

    def retrieve(
        self,
        query: Query
    ) -> RetrievalResult:

        vector_results = self.vector_retriever.retrieve(
            query
        )

        bm25_results = self.bm25_retriever.retrieve(
            query
        )

        graph_result = self.graph_retriever.retrieve(
            query
        )

        return RetrievalResult(
            vector_results=vector_results,
            bm25_results=bm25_results,
            graph_result=graph_result
        )
from app.online.models import OnlineState
from app.online.retrievers.hybrid_retriever import HybridRetriever
from app.online.retrievers.vector_retriever import VectorRetriever
from app.online.retrievers.bm25_retriever import BM25Retriever
from app.online.retrievers.graph_retriever import GraphRetriever

from app.online.implementations.mock.mock_vector import MockVectorRetriever
from app.online.implementations.mock.mock_bm25 import MockBM25Retriever
from app.online.implementations.mock.mock_graph import MockGraphRetriever


class HybridRetrieverNode:

    def __init__(self):

        vector = VectorRetriever(
            MockVectorRetriever()
        )

        bm25 = BM25Retriever(
            MockBM25Retriever()
        )

        graph = GraphRetriever(
            MockGraphRetriever()
        )

        self.retriever = HybridRetriever(
            vector,
            bm25,
            graph
        )

    def __call__(
        self,
        state: OnlineState
    ) -> OnlineState:

        state.retrieval = self.retriever.retrieve(
            state.query
        )

        return state
from app.online.models import OnlineState
from app.online.services.reranker import Reranker


class RerankerNode:

    def __init__(self):

        self.reranker = Reranker()

    def __call__(
        self,
        state: OnlineState
    ) -> OnlineState:

        state.ranked_chunks = self.reranker.rerank(
            state.retrieval
        )

        return state
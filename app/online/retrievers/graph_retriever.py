from app.online.interfaces.base_graph import BaseGraphRetriever
from app.online.models import GraphResult, Query


class GraphRetriever:

    def __init__(
        self,
        graph_store: BaseGraphRetriever
    ):
        self.graph_store = graph_store

    def retrieve(
        self,
        query: Query
    ) -> GraphResult:

        return self.graph_store.search(query)
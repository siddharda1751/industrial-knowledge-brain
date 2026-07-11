from app.online.implementations.mock.mock_data import MOCK_GRAPH
from app.online.interfaces.base_graph import BaseGraphRetriever
from app.online.models import GraphResult, Query


class MockGraphRetriever(BaseGraphRetriever):

    def search(
        self,
        query: Query
    ) -> GraphResult:

        for entity in query.entities:

            if entity in MOCK_GRAPH:

                return MOCK_GRAPH[entity]

        return GraphResult()
from app.online.models import OnlineState
from app.online.services.query_analyzer import QueryAnalyzer


class QueryAnalyzerNode:

    def __init__(self):

        self.analyzer = QueryAnalyzer()

    def __call__(
        self,
        state: OnlineState
    ) -> OnlineState:

        state.query = self.analyzer.analyze(
            state.query
        )

        return state
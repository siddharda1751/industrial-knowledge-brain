from app.online.models import OnlineState, Query
from app.online.pipeline import build_graph


graph = build_graph()

state = OnlineState(
    query=Query(
        query="Explain Steam Drum"
    )
)

result = graph.invoke(state)

print(result)
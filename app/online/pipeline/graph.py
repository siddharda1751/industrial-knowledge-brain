from langgraph.graph import END, START, StateGraph

from app.online.models import OnlineState

from app.online.nodes.query_analyzer import QueryAnalyzerNode
from app.online.nodes.hybrid_retriever import HybridRetrieverNode
from app.online.nodes.reranker import RerankerNode
from app.online.nodes.context_builder import ContextBuilderNode
from app.online.nodes.llm_node import LLMNode


def build_graph():

    builder = StateGraph(OnlineState)

    builder.add_node(
        "query_analyzer",
        QueryAnalyzerNode()
    )

    builder.add_node(
        "retriever",
        HybridRetrieverNode()
    )

    builder.add_node(
        "reranker",
        RerankerNode()
    )

    builder.add_node(
        "context_builder",
        ContextBuilderNode()
    )

    builder.add_node(
        "llm",
        LLMNode()
    )

    builder.add_edge(
        START,
        "query_analyzer"
    )

    builder.add_edge(
        "query_analyzer",
        "retriever"
    )

    builder.add_edge(
        "retriever",
        "reranker"
    )

    builder.add_edge(
        "reranker",
        "context_builder"
    )

    builder.add_edge(
        "context_builder",
        "llm"
    )

    builder.add_edge(
        "llm",
        END
    )

    return builder.compile()
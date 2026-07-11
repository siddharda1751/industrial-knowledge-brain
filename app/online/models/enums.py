from enum import Enum


class QueryIntent(str, Enum):
    QA = "qa"
    PROCEDURE = "procedure"
    TROUBLESHOOTING = "troubleshooting"
    COMPARISON = "comparison"
    SUMMARY = "summary"
    UNKNOWN = "unknown"


class RetrievalSource(str, Enum):
    VECTOR = "vector"
    BM25 = "bm25"
    GRAPH = "graph"
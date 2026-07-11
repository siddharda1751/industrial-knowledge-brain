from typing import Any
from pydantic import BaseModel, Field
from .enums import RetrievalSource

class RetrievedChunk(BaseModel):
    chunk_id: str

    doc_id: str

    score: float

    source: RetrievalSource

    text_summary: str = ""

    table_summary: str = ""

    image_summary: str = ""

    metadata: dict[str, Any] = Field(default_factory=dict)


class GraphResult(BaseModel):
    entities: list[str] = Field(default_factory=list)

    relationships: list[str] = Field(default_factory=list)

    chunk_ids: list[str] = Field(default_factory=list)


class RetrievalResult(BaseModel):
    vector_results: list[RetrievedChunk] = Field(default_factory=list)

    bm25_results: list[RetrievedChunk] = Field(default_factory=list)

    graph_result: GraphResult = Field(default_factory=GraphResult)
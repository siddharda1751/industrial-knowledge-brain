from pydantic import BaseModel, Field

from .document import DocumentChunk


class Context(BaseModel):
    documents: list[DocumentChunk] = Field(default_factory=list)

    graph_context: str = ""

    prompt: str = ""

    citations: list[str] = Field(default_factory=list)
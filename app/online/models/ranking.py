from pydantic import BaseModel, Field

from .enums import RetrievalSource
from .retrieval import RetrievedChunk


class RankedChunk(BaseModel):

    chunk: RetrievedChunk

    final_score: float

    retrieval_sources: list[RetrievalSource] = Field(
        default_factory=list
    )
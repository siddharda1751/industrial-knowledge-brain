from pydantic import BaseModel, Field

from .answer import Answer
from .context import Context
from .document import DocumentChunk
from .query import Query
from .ranking import RankedChunk
from .retrieval import RetrievalResult


class OnlineState(BaseModel):
    query: Query

    retrieval: RetrievalResult = Field(
        default_factory=RetrievalResult
    )

    ranked_chunks: list[RankedChunk] = Field(
        default_factory=list
    )

    documents: list[DocumentChunk] = Field(
        default_factory=list
    )

    context: Context = Field(
        default_factory=Context
    )

    answer: Answer = Field(
        default_factory=Answer
    )

    history: list[str] = Field(
        default_factory=list
    )
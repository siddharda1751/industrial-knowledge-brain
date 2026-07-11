from typing import Any
from pydantic import BaseModel, Field
from .enums import QueryIntent


class Query(BaseModel):
    query: str

    intent: QueryIntent = QueryIntent.UNKNOWN

    entities: list[str] = Field(default_factory=list)

    filters: dict[str, Any] = Field(default_factory=dict)
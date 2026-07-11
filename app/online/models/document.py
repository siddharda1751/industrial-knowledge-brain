from typing import Any

from pydantic import BaseModel, Field


class TableContent(BaseModel):
    table_id: str = ""

    content: str = ""

    summary: str = ""

    metadata: dict[str, Any] = Field(default_factory=dict)


class ImageContent(BaseModel):
    image_id: str = ""

    image_path: str = ""

    summary: str = ""

    metadata: dict[str, Any] = Field(default_factory=dict)


class DocumentChunk(BaseModel):
    chunk_id: str

    doc_id: str

    original_text: str = ""

    tables: list[TableContent] = Field(default_factory=list)

    images: list[ImageContent] = Field(default_factory=list)

    metadata: dict[str, Any] = Field(default_factory=dict)
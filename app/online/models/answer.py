from pydantic import BaseModel, Field


class Answer(BaseModel):
    response: str = ""

    citations: list[str] = Field(default_factory=list)
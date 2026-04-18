from pydantic import BaseModel
from typing import List


class RetrievedChunk(BaseModel):
    text: str
    score: float


class QueryResponse(BaseModel):
    query: str
    answer: str
    retrieved_chunks: List[RetrievedChunk]

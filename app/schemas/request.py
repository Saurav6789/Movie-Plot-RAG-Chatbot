from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, description="User question.")
    top_k: int = Field(
        default=3, ge=1, le=10, description="Number of chunks to retrieve."
    )

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    azure_openai_api_key: str = Field(
        ..., description="Azure OpenAI API key. Must not be in git."
    )
    azure_openai_endpoint: str = Field(..., description="Azure OpenAI endpoint URL.")
    azure_deployment_name: str = Field(
        "gpt-4o-mini", description="Name of the completion deployment."
    )
    azure_embedding_deployment: str = Field(
        "text-embedding-3-large", description="Name of the embedding deployment."
    )
    azure_completion_version: str = Field(
        "2024-08-01-preview", description="API version for chat completions."
    )
    azure_embedding_version: str = Field(
        "2023-05-15", description="API version for embeddings."
    )
    chunk_size: int = Field(
        500, ge=100, le=4096, description="Maximum chunk size in characters."
    )
    chunk_overlap: int = Field(50, ge=0, le=200, description="Overlap between chunks.")
    top_k: int = Field(3, ge=1, le=20, description="Number of chunks to retrieve.")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings(_env_file=Path(__file__).parent.parent / ".env")

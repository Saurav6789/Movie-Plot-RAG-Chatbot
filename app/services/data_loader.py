import pandas as pd
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import settings


class DataLoader:
    """
    Handles loading and preprocessing of text data for RAG pipeline.
    """

    def __init__(
        self,
        file_path: str = "data/wiki_movie_plots.csv",
        limit: int = 200,
        use_sampling: bool = True,
    ):
        self.file_path = file_path
        self.limit = limit
        self.use_sampling = use_sampling

    def load_documents(self) -> List[str]:
        """
        Load and preprocess documents from CSV.

        Returns:
            List[str]: Cleaned document strings
        """

        # Load CSV
        df = pd.read_csv(self.file_path)

        # Drop missing values
        df = df.dropna(subset=["Plot", "Title"])

        # Limit dataset size
        if self.use_sampling:
            df = df.sample(n=min(self.limit, len(df)), random_state=42)
        else:
            df = df.head(self.limit)

        # Combine metadata + text
        documents = [
            f"Title: {row['Title']}\n"
            f"Genre: {row.get('Genre', 'Unknown')}\n"
            f"Plot: {row['Plot']}"
            for _, row in df.iterrows()
        ]

        return documents

    def split_documents(self, documents: List[str]) -> List[str]:
        """
        Split documents into chunks.

        Args:
            documents (List[str])

        Returns:
            List[str]: Text chunks
        """

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
        )

        chunks = []
        for doc in documents:
            chunks.extend(splitter.split_text(doc))

        return chunks

from openai import AzureOpenAI
import numpy as np
from config import settings


class EmbeddingStore:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=settings.azure_openai_api_key,
            api_version=settings.azure_embedding_version,
            azure_endpoint=settings.azure_openai_endpoint,
        )
        self.documents = []
        self.embeddings = []

    def embed(self, texts):
        response = self.client.embeddings.create(
            model=settings.azure_embedding_deployment,
            input=texts,
        )
        return [d.embedding for d in response.data]

    def index(self, chunks):
        self.documents = chunks
        self.embeddings = self.embed(chunks)

    def cosine(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def retrieve(self, query_embedding, top_k):
        scores = [
            {"text": doc, "score": self.cosine(e, query_embedding)}
            for doc, e in zip(self.documents, self.embeddings)
        ]
        scores.sort(key=lambda x: x["score"], reverse=True)
        return scores[:top_k]

from fastapi import FastAPI
from contextlib import asynccontextmanager
from services.embedding_store import EmbeddingStore
from services.llm import LLMService
from services.data_loader import DataLoader
from routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    store = EmbeddingStore()
    llm = LLMService()
    loader = DataLoader()
    docs = loader.load_documents()
    chunks = loader.split_documents(docs)

    store.index(chunks)

    app.state.store
    router.llm = llm

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)

from fastapi import APIRouter, Depends, Request
from schemas.request import QueryRequest
from schemas.response import QueryResponse

router = APIRouter()


# Dependency to access store
def get_store(request: Request):
    return request.app.state.store


def get_llm(request: Request):
    return request.app.state.llm


# ✅ Health check endpoint
@router.get("/health")
def health():
    return {"status": "ok"}


# ✅ Main RAG endpoint
@router.post("/ask", response_model=QueryResponse)
def ask(request_data: QueryRequest, request: Request):
    store = get_store(request)
    llm = get_llm(request)

    query_embedding = store.embed([request_data.query])[0]
    retrieved = store.retrieve(query_embedding, request_data.top_k)

    context = "\n\n".join([doc["text"] for doc in retrieved])
    answer = llm.generate(request_data.query, context)

    return {
        "query": request_data.query,
        "answer": answer,
        "retrieved_chunks": retrieved,
    }

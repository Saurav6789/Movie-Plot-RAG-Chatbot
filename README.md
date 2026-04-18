# Movie Plot RAG Chatbot

A FastAPI‑based RAG service that answers movie‑related questions using vector search over a movie‑plot dataset and Azure OpenAI.

## 📦 Prerequisites

- Python 3.10+ (you’re using 3.14)
- [`uv`](https://github.com/astral-sh/uv) installed
- Azure OpenAI resource with:
  - Embedding deployment named `text-embedding-3-large`
  - Completion deployment if you use `gpt-4o-mini` (or adjust name in `.env`)

## 🛠️ Setup with `uv` (no requirements.txt)

1. **Clone the project**

```bash
git clone https://github.com/.../saurav-anand-TT.git  # or your repo
cd saurav-anand-TT
```

2. **Create a virtual environment**

```bash
uv venv
source .venv/bin/activate    # Linux/macOS
# or
.venv\Scripts\activate       # Windows
```

3. **Install dependencies**


```bash
uv add fastapi uvicorn openai pandas langchain-text-splitters pydantic pydantic-settings
```

(This assumes your code uses `FastAPI`, `openai`, `pandas`, `langchain_text_splitters`, and `pydantic`.) [web:31][web:32]

4. **Prepare the dataset**

- Download the `wiki_movie_plots.csv` dataset (e.g., from Kaggle or other sources).
- Place it at:

```bash
saurav-anand-TT/app/data/wiki_movie_plots.csv
```

5. **Configure Azure OpenAI**

Create/edit `.env` in the root directory:

```ini
AZURE_OPENAI_API_KEY=<key-from-azure-keys-and-endpoint>
AZURE_OPENAI_ENDPOINT=https://open-ai-resource-rob.openai.azure.com/

AZURE_DEPLOYMENT_NAME=gpt-4o-mini
AZURE_EMBEDDING_DEPLOYMENT=text-embedding-3-large

AZURE_COMPLETION_VERSION=2024-08-01-preview
AZURE_EMBEDDING_VERSION=2023-05-15

CHUNK_SIZE=500
CHUNK_OVERLAP=50
TOP_K=3
```

> Replace `<key-from-azure-keys-and-endpoint>` with a valid Azure OpenAI API key and ensure the endpoint URL matches exactly what Azure shows.

## 🚀 Run the app

```bash
cd app
uv run uvicorn main:app --reload
```

The server will start at: http://127.0.0.1:8000


It will:
- Load `wiki_movie_plots.csv`.
- Split texts into chunks.
- Compute embeddings and index them on startup.

## 🧩 API Endpoints

### Health check

```bash
curl http://127.0.0.1:8000/health
```

Response:
```json
{"status":"ok"}
```

### Ask questions (RAG endpoint)

```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Tell me about a movie plot involving a superhero",
    "top_k": 3
  }'
```

Response:
```json
{
  "query": "Tell me about a movie plot involving a superhero",
  "answer": "...",
  "retrieved_chunks": [
    {"text": "...", "score": 0.92},
    ...
  ]
}
```

## ⚠️ Common issues

- `FileNotFoundError: 'data/wiki_movie_plots.csv'`  
  → Ensure the CSV exists at `app/data/wiki_movie_plots.csv`.

- `openai.AuthenticationError: 401`  
  → Double‑check `.env`:
  - `AZURE_OPENAI_API_KEY` matches the key in **Azure → Keys and Endpoint**.
  - `AZURE_OPENAI_ENDPOINT` is the exact endpoint URL.
  - `AZURE_EMBEDDING_DEPLOYMENT` matches the deployment name in Azure.

- `ImportError: cannot import name 'load_documents'`  
  → Make sure you’re using the `DataLoader` class and not calling `load_documents` as a top‑level function (unless you added helper functions).

## 📚 Project structure

```text
.
├── .env
├── main.py
└── app/
    ├── main.py
    ├── config.py
    ├── schemas/
    │   ├── request.py
    │   └── response.py
    ├── services/
    │   ├── data_loader.py
    │   ├── embedding_store.py
    │   ├── llm.py
    │   ├── prompt.py
    │   └── evaluation.py
    ├── routes.py
    └── data/
        └── wiki_movie_plots.csv
```

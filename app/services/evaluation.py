def evaluate_retrieval(retrieved_docs, query):
    return any(query.lower() in doc["text"].lower() for doc in retrieved_docs)

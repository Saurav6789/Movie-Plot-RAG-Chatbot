from services.embedding_store import AzureEmbeddingStore


def test_cosine_similarity():
    store = AzureEmbeddingStore()

    a = [1, 0]
    b = [1, 0]

    score = store.cosine_similarity(a, b)

    assert score == 1.0

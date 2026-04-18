from services.data_loader import DataLoader


def test_load_documents_returns_list():
    loader = DataLoader(file_path="data/wiki_movie_plots.csv", limit=5)

    docs = loader.load_documents()

    assert isinstance(docs, list)
    assert len(docs) <= 5
    assert isinstance(docs[0], str)


def test_split_documents():
    loader = DataLoader()

    docs = ["This is a test document about AI. " * 20]
    chunks = loader.split_documents(docs)

    assert isinstance(chunks, list)
    assert len(chunks) > 1  # should split into multiple chunks

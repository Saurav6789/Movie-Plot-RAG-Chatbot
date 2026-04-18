from services.prompt import build_rag_prompt


def test_prompt_contains_context_and_query():
    context = "Movie: Titanic plot summary"
    query = "What is Titanic about?"

    prompt = build_rag_prompt(context, query)

    assert "Titanic" in prompt
    assert query in prompt
    assert "STRICT RULES" in prompt
    assert "CONTEXT" in prompt

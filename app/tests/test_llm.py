from services.llm import LLMService
from unittest.mock import MagicMock
import services.llm as llm_module


def test_llm_generate(monkeypatch):
    service = LLMService()

    # Mock response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Mocked answer"))]

    # Patch Azure client
    service.client.chat.completions.create = MagicMock(return_value=mock_response)

    result = service.generate("What is AI?", "AI is intelligence")

    assert result == "Mocked answer"

from openai import AzureOpenAI
from config import settings
from services.prompt import build_rag_prompt


class LLMService:
    """
    Handles interaction with Azure OpenAI LLM.
    """

    def __init__(self):
        self.client = AzureOpenAI(
            api_key=settings.azure_openai_api_key,
            api_version=settings.azure_completion_version,
            azure_endpoint=settings.azure_openai_endpoint,
        )

        self.deployment_name = settings.azure_deployment_name

    def generate(self, query: str, context: str) -> str:
        """
        Generate answer using RAG context.
        """

        prompt = build_rag_prompt(context, query)

        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that follows instructions strictly.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=messages,
                temperature=0.2,
                max_tokens=500,
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Error generating response: {str(e)}"

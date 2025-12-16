import asyncio

class LLMClient:
    """
    Mockable LLM client.
    In production this would call watsonx/OpenAI/etc.
    """

    async def generate(self, prompt: str) -> str:
        # Deterministic output (great for testing + CI)
        await asyncio.sleep(0)
        return f"[SAFE_MOCK_RESPONSE] {prompt}"

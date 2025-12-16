from fastapi import FastAPI
from pydantic import BaseModel

from app.llm_client import LLMClient
from app.guardrails.policy import GuardrailPolicy


app = FastAPI(title="Secure AI DevOps Pipeline")

llm = LLMClient()
policy = GuardrailPolicy()

# ---------- Request / Response Models ----------
class ChatRequest(BaseModel):
    user_id: str
    message: str
    
class ChatResponse(BaseModel):
    allowed: bool
    reason: str
    response: str | None = None

# ---------- Endpoints ----------

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    decision = policy.evaluate(req.message)

    if not decision["allowed"]:
        return ChatResponse(
            allowed=False,
            reason="; ".join(decision["reasons"]),
            response=None,
        )

    model_output = await llm.generate(req.message)

    return ChatResponse(
        allowed=True,
        reason="OK",
        response=model_output,
    )

from fastapi import FastAPI
from pydantic import BaseModel

from app.llm_client import LLMClient

app = FastAPI(title="Secure AI DevOps Pipeline")

llm = LLMClient()

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    model_output = await llm.generate(req.message)
    return ChatResponse(response=model_output)

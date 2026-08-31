from pydantic import BaseModel
from typing import Optional

class AIQueryRequest(BaseModel):
    prompt: str
    context: Optional[dict] = None

class AIQueryResponse(BaseModel):
    answer: str
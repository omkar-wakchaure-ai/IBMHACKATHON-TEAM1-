from pydantic import BaseModel
from typing import Optional

class WhatsAppOrderRequest(BaseModel):
    supplier_id: str
    product_name: str
    quantity: float
    
class WhatsAppResponse(BaseModel):
    status: str
    message_sid: Optional[str] = None
    error: Optional[str] = None
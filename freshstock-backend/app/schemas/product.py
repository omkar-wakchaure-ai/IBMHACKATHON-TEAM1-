from pydantic import BaseModel
from datetime import date

class ProductBase(BaseModel):
    name: str
    supplier: str
    manufacturing_date: date
    expiry_date: date
    quantity: float
    unit_price: float

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    freshness_score: float
    
    class Config:
        from_attributes = True
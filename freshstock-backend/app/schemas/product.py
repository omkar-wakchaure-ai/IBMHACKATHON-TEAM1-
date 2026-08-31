from datetime import date
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    category: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)
    expiry_date: date | None = None
    supplier_id: str | None = None


class Product(ProductCreate):
    id: int
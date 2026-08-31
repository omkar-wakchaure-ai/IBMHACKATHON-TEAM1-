from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from typing import List
from pydantic import BaseModel

from app.core.database import get_db
from app.models.product import Product

router = APIRouter()

# Pydantic schemas for request validation
class ProductCreate(BaseModel):
    name: str
    supplier: str
    manufacturing_date: date
    expiry_date: date
    quantity: float
    unit_price: float

class ProductResponse(ProductCreate):
    id: int
    freshness_score: float
    
    class Config:
        from_attributes = True # updated for Pydantic v2

@router.post("/", response_model=ProductResponse)
def ingest_product(product: ProductCreate, db: Session = Depends(get_db)):
    # Calculate initial freshness score dynamically
    total_shelf_life = (product.expiry_date - product.manufacturing_date).days
    days_left = (product.expiry_date - date.today()).days
    
    freshness = 100.0
    if total_shelf_life > 0:
        freshness = max(0.0, (days_left / total_shelf_life) * 100)

    db_product = Product(
        name=product.name,
        supplier=product.supplier,
        manufacturing_date=product.manufacturing_date,
        expiry_date=product.expiry_date,
        quantity=product.quantity,
        unit_price=product.unit_price,
        freshness_score=freshness
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=List[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
from fastapi import APIRouter, status

from app.schemas.product import Product, ProductCreate
from app.services.inventory_service import (
    get_all_products,
    create_product,
)


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("/", response_model=list[Product])
def get_products():
    return get_all_products()


@router.post(
    "/",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
)
def add_product(product_data: ProductCreate):
    return create_product(product_data)
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.product import Product, ProductCreate
from app.services.inventory_service import (
    get_all_products,
    get_product,
    create_product,
    update_product,
    delete_product,
    get_low_stock_products,
    get_expiring_products,
)


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


# ---------------------------------------------------------
# GET ALL PRODUCTS
# ---------------------------------------------------------

@router.get("/", response_model=list[Product])
def get_products(db: Session = Depends(get_db)):
    return get_all_products(db)


# ---------------------------------------------------------
# GET SINGLE PRODUCT
# ---------------------------------------------------------

@router.get("/{product_id}", response_model=Product)
def get_single_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    product = get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product


# ---------------------------------------------------------
# CREATE PRODUCT
# ---------------------------------------------------------

@router.post(
    "/",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
)
def add_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db),
):
    return create_product(db, product_data)


# ---------------------------------------------------------
# UPDATE PRODUCT
# ---------------------------------------------------------

@router.put(
    "/{product_id}",
    response_model=Product,
)
def update_product_endpoint(
    product_id: int,
    product_data: ProductCreate,
    db: Session = Depends(get_db),
):
    product = update_product(
        db,
        product_id,
        product_data,
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product


# ---------------------------------------------------------
# DELETE PRODUCT
# ---------------------------------------------------------

@router.delete("/{product_id}")
def remove_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_product(
        db,
        product_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return {
        "message": "Product deleted successfully",
        "product_id": product_id,
    }


# ---------------------------------------------------------
# LOW STOCK PRODUCTS
# ---------------------------------------------------------

@router.get(
    "/alerts/low-stock",
    response_model=list[Product],
)
def low_stock_products(
    db: Session = Depends(get_db),
):
    return get_low_stock_products(db)


# ---------------------------------------------------------
# EXPIRING PRODUCTS
# ---------------------------------------------------------

@router.get(
    "/alerts/expiring",
    response_model=list[Product],
)
def expiring_products(
    db: Session = Depends(get_db),
):
    return get_expiring_products(db)

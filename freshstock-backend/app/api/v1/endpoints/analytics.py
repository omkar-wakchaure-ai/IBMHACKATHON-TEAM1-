from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.product import Product as ProductModel


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/summary")
def inventory_summary(
    db: Session = Depends(get_db)
):
    products = db.query(ProductModel).all()

    total_products = len(products)

    total_quantity = sum(
        product.quantity
        for product in products
    )

    low_stock_count = sum(
        1
        for product in products
        if product.quantity <= 10
    )

    expiring_count = 0

    from datetime import date, timedelta

    today = date.today()
    expiry_limit = today + timedelta(days=7)

    for product in products:
        if (
            product.expiry_date is not None
            and today <= product.expiry_date <= expiry_limit
        ):
            expiring_count += 1

    return {
        "total_products": total_products,
        "total_quantity": total_quantity,
        "low_stock_count": low_stock_count,
        "expiring_soon_count": expiring_count,
    }
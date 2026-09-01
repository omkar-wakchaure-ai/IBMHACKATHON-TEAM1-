from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.product import Product as ProductModel

from app.services.demand_prediction_service import predict_restock_need
from app.services.inventory_risk_service import generate_inventory_risk_report

from app.services.ml_prediction_service import (
    predict_demand,
    calculate_restock_quantity,
    generate_inventory_recommendations,
    expiry_recommendation
)


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


# ---------------------------------------------------------
# RESTOCK PREDICTION
# ---------------------------------------------------------

@router.get("/restock-prediction")
def restock_prediction(
    db: Session = Depends(get_db)
):
    return predict_restock_need(db)


# ---------------------------------------------------------
# DEMAND PREDICTION
# ---------------------------------------------------------

@router.get("/demand-prediction")
def demand_prediction():
    return predict_demand()


# ---------------------------------------------------------
# RESTOCK RECOMMENDATION FOR ONE PRODUCT
# ---------------------------------------------------------

@router.get("/restock-recommendation/{product_id}")
def restock_recommendation(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = (
        db.query(ProductModel)
        .filter(ProductModel.id == product_id)
        .first()
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    demand_result = predict_demand()

    return calculate_restock_quantity(
        product.quantity,
        demand_result["predicted_demand"]
    )


# ---------------------------------------------------------
# INVENTORY RECOMMENDATIONS FOR ALL PRODUCTS
# ---------------------------------------------------------

@router.get("/inventory-recommendations")
def inventory_recommendations(
    db: Session = Depends(get_db)
):

    return generate_inventory_recommendations(db)


# ---------------------------------------------------------
# EXPIRY RECOMMENDATION
# ---------------------------------------------------------

@router.get("/expiry-recommendation/{product_id}")
def expiry_product_recommendation(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = (
        db.query(ProductModel)
        .filter(ProductModel.id == product_id)
        .first()
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "product_id": product.id,
        "product_name": product.name,
        **expiry_recommendation(
            product.expiry_date,
            product.quantity
        )
    }
# ---------------------------------------------------------
# INVENTORY RISK REPORT
# ---------------------------------------------------------

@router.get("/inventory-risk")
def inventory_risk(
    db: Session = Depends(get_db)
):
    return generate_inventory_risk_report(db)
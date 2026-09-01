from datetime import date

from app.models.product import Product as ProductModel
from app.services.ml_prediction_service import predict_demand


def generate_assistant_response(db, product_id: int):

    product = (
        db.query(ProductModel)
        .filter(ProductModel.id == product_id)
        .first()
    )

    if product is None:
        return None

    # Product-specific demand prediction
    demand_result = predict_demand(product_id)
    expected_demand = demand_result["predicted_demand"]

    # Calculate days until expiry
    if product.expiry_date:
        days_to_expiry = (product.expiry_date - date.today()).days
    else:
        days_to_expiry = None

    # Calculate waste risk
    if days_to_expiry is not None:
        excess_stock = product.quantity - expected_demand

        if days_to_expiry <= 1 and excess_stock > 0:
            waste_risk = "HIGH"
        elif days_to_expiry <= 3 and excess_stock > 0:
            waste_risk = "MEDIUM"
        else:
            waste_risk = "LOW"
    else:
        waste_risk = "UNKNOWN"

    # Generate recommendation
    if days_to_expiry is not None and days_to_expiry < 0:
        recommendation = "Remove expired stock immediately."

    elif (
        days_to_expiry is not None
        and days_to_expiry <= 3
        and product.quantity > expected_demand
    ):
        recommendation = (
            "Prioritize selling this product immediately "
            "through discounts to reduce waste."
        )

    elif product.quantity < expected_demand:
        recommendation = (
            "Restock this product because current inventory "
            "is below predicted demand."
        )

    elif product.quantity > expected_demand * 2:
        recommendation = (
            "Avoid additional purchasing because inventory "
            "is significantly higher than predicted demand."
        )

    else:
        recommendation = (
            "Inventory level is healthy. Continue monitoring demand."
        )

    return {
        "product_id": product.id,
        "product_name": product.name,
        "current_stock": product.quantity,
        "expected_demand": expected_demand,
        "days_to_expiry": days_to_expiry,
        "waste_risk": waste_risk,
        "recommendation": recommendation
    }
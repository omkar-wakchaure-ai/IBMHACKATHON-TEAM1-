import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def predict_demand():
    # Historical sales data
    data = {
        "day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "quantity_sold": [5, 7, 6, 8, 10, 9, 12, 11, 13, 15],
    }

    df = pd.DataFrame(data)

    X = df[["day"]]
    y = df["quantity_sold"]

    # Train ML model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    # Predict next-day demand
    next_day = pd.DataFrame({
        "day": [11]
    })

    prediction = model.predict(next_day)[0]

    predicted_demand = round(float(prediction), 2)

    return {
        "next_day": 11,
        "predicted_demand": predicted_demand
    }


def calculate_restock_quantity(
    current_quantity: int,
    predicted_demand: float
):
    recommended_stock = predicted_demand * 2

    restock_quantity = max(
        0,
        round(recommended_stock - current_quantity)
    )

    if restock_quantity == 0:
        recommendation = "NO RESTOCK REQUIRED"
    elif restock_quantity <= 10:
        recommendation = "RESTOCK SMALL QUANTITY"
    else:
        recommendation = "RESTOCK NOW"

    return {
        "current_quantity": current_quantity,
        "predicted_demand": predicted_demand,
        "recommended_stock": round(recommended_stock, 2),
        "restock_quantity": restock_quantity,
        "recommendation": recommendation
    }
def generate_inventory_recommendations(db):
    from app.models.product import Product as ProductModel

    products = db.query(ProductModel).all()

    demand_result = predict_demand()
    predicted_demand = demand_result["predicted_demand"]

    recommendations = []

    for product in products:

        result = calculate_restock_quantity(
            product.quantity,
            predicted_demand
        )

        recommendations.append({
            "product_id": product.id,
            "product_name": product.name,
            "category": product.category,
            "current_quantity": product.quantity,
            "predicted_demand": predicted_demand,
            "recommended_stock": result["recommended_stock"],
            "restock_quantity": result["restock_quantity"],
            "recommendation": result["recommendation"]
        })

    return recommendations

from datetime import date


def expiry_recommendation(
    expiry_date,
    current_quantity: int
):
    if expiry_date is None:
        return {
            "expiry_status": "NO EXPIRY DATE",
            "recommendation": "NORMAL INVENTORY"
        }

    today = date.today()
    days_remaining = (expiry_date - today).days

    if days_remaining < 0:
        recommendation = "EXPIRED - REMOVE FROM STOCK"
        status = "EXPIRED"

    elif days_remaining <= 3:
        recommendation = "URGENT DISCOUNT / SELL NOW"
        status = "CRITICAL"

    elif days_remaining <= 7:
        recommendation = "DISCOUNT / SELL SOON"
        status = "EXPIRING SOON"

    else:
        recommendation = "NORMAL INVENTORY"
        status = "SAFE"

    return {
        "expiry_status": status,
        "days_until_expiry": days_remaining,
        "current_quantity": current_quantity,
        "recommendation": recommendation
    }
import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


# ---------------------------------------------------------
# LOAD HISTORICAL SALES DATA
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

SALES_FILE = os.path.join(
    BASE_DIR,
    "data",
    "historical_sales.csv"
)


# ---------------------------------------------------------
# PREDICT DEMAND FOR A PRODUCT
# ---------------------------------------------------------

def predict_demand(product_id: int = None):

    df = pd.read_csv(SALES_FILE)

    if product_id is not None:
        df = df[df["product_id"] == product_id]

    if df.empty:
        return {
            "next_day": 1,
            "predicted_demand": 0.0
        }

    # Create sequential day numbers for the ML model
    df = df.copy()
    df["day"] = range(1, len(df) + 1)

    X = df[["day"]]
    y = df["quantity_sold"]

    # Train Random Forest model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    # Predict next day
    next_day = len(df) + 1

    next_day_data = pd.DataFrame({
        "day": [next_day]
    })

    prediction = model.predict(next_day_data)[0]

    return {
        "next_day": next_day,
        "predicted_demand": round(float(prediction), 2)
    }


# ---------------------------------------------------------
# CALCULATE RESTOCK QUANTITY
# ---------------------------------------------------------

def calculate_restock_quantity(
    current_quantity: int,
    predicted_demand: float
):

    # Keep 2 days of predicted demand as target stock
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


# ---------------------------------------------------------
# INVENTORY RECOMMENDATIONS FOR ALL PRODUCTS
# ---------------------------------------------------------

def generate_inventory_recommendations(db):

    from app.models.product import Product as ProductModel

    products = db.query(ProductModel).all()

    recommendations = []

    for product in products:

        demand_result = predict_demand(product.id)

        predicted_demand = demand_result["predicted_demand"]

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


# ---------------------------------------------------------
# EXPIRY RECOMMENDATION
# ---------------------------------------------------------

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

    days_remaining = (
        expiry_date - today
    ).days

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
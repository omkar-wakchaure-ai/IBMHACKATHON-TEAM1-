"""
FreshStock AI - Inventory Optimization
"""

import sys
import os

# Allow importing from the project root
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from ai.forecasting.predict import predict_recent_demand


def calculate_recommendation(
    predicted_demand,
    current_stock,
    incoming_stock=0,
    safety_stock=0
):
    """Calculate inventory recommendation."""

    available_stock = current_stock + incoming_stock

    recommended_inventory = predicted_demand + safety_stock

    order_quantity = max(
        0,
        recommended_inventory - available_stock
    )

    if predicted_demand > 0:
        coverage = available_stock / predicted_demand
    else:
        coverage = 999

    if coverage < 0.5:
        stockout_risk = "HIGH"
    elif coverage < 1:
        stockout_risk = "MEDIUM"
    else:
        stockout_risk = "LOW"

    return {
        "predicted_demand": round(predicted_demand, 2),
        "current_stock": round(current_stock, 2),
        "incoming_stock": round(incoming_stock, 2),
        "available_stock": round(available_stock, 2),
        "safety_stock": round(safety_stock, 2),
        "recommended_inventory": round(
            recommended_inventory, 2
        ),
        "recommended_order": round(
            order_quantity, 2
        ),
        "stockout_risk": stockout_risk
    }


def generate_inventory_recommendation(
    product="BEVERAGES",
    store=1,
    current_stock=1500,
    incoming_stock=300,
    safety_stock=200
):
    """
    Complete FreshStock pipeline:

    Forecast → Inventory Optimization
    """

    # Get prediction from trained XGBoost model
    forecast = predict_recent_demand(
        product=product,
        store=store
    )

    predicted_demand = forecast["predicted_demand"]

    # Calculate inventory recommendation
    recommendation = calculate_recommendation(
        predicted_demand=predicted_demand,
        current_stock=current_stock,
        incoming_stock=incoming_stock,
        safety_stock=safety_stock
    )

    # Add product/store information
    recommendation["product"] = product
    recommendation["store"] = store

    return recommendation


if __name__ == "__main__":

    result = generate_inventory_recommendation(
        product="BEVERAGES",
        store=1,
        current_stock=1500,
        incoming_stock=300,
        safety_stock=200
    )

    print("\n======================================")
    print("      FreshStock AI Recommendation")
    print("======================================")

    print(f"Product: {result['product']}")
    print(f"Store: {result['store']}")

    print(
        f"\nPredicted Demand: "
        f"{result['predicted_demand']}"
    )

    print(
        f"Current Stock: "
        f"{result['current_stock']}"
    )

    print(
        f"Incoming Stock: "
        f"{result['incoming_stock']}"
    )

    print(
        f"Available Stock: "
        f"{result['available_stock']}"
    )

    print(
        f"Safety Stock: "
        f"{result['safety_stock']}"
    )

    print(
        f"\nRecommended Inventory: "
        f"{result['recommended_inventory']}"
    )

    print(
        f"Recommended Order: "
        f"{result['recommended_order']}"
    )

    print(
        f"Stock-out Risk: "
        f"{result['stockout_risk']}"
    )

    print("======================================")
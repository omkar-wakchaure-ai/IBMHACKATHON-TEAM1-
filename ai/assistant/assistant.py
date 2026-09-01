"""
FreshStock AI - Unified AI Assistant

Connects:
1. Demand Forecasting
2. Inventory Optimization
3. Waste Risk Detection
"""

from ai.forecasting.predict import predict_recent_demand
from ai.inventory.optimizer import calculate_recommendation
from ai.waste.risk import calculate_waste_risk
from ai.granite.client import generate_ai_recommendation

def analyze_product(
    product="BEVERAGES",
    store=1,
    current_stock=1500,
    incoming_stock=300,
    safety_stock=200,
    days_to_expiry=3
):
    """
    Run the complete FreshStock AI analysis.
    """

    # ----------------------------------------
    # 1. Demand Forecasting
    # ----------------------------------------

    forecast = predict_recent_demand(
        product=product,
        store=store
    )

    predicted_demand = forecast["predicted_demand"]

    # ----------------------------------------
    # 2. Inventory Optimization
    # ----------------------------------------

    inventory = calculate_recommendation(
        predicted_demand=predicted_demand,
        current_stock=current_stock,
        incoming_stock=incoming_stock,
        safety_stock=safety_stock
    )

    # ----------------------------------------
    # 3. Waste Risk
    # ----------------------------------------

    waste = calculate_waste_risk(
        current_stock=current_stock,
        predicted_demand=predicted_demand,
        incoming_stock=incoming_stock,
        days_to_expiry=days_to_expiry
    )

    # ----------------------------------------
    # 4. Combine Results
    # ----------------------------------------

    result = {
        "product": product,
        "store": store,

        "forecast": {
            "predicted_demand": predicted_demand
        },

        "inventory": {
            "current_stock": current_stock,
            "incoming_stock": incoming_stock,
            "recommended_order": inventory[
                "recommended_order"
            ],
            "stockout_risk": inventory[
                "stockout_risk"
            ]
        },

        "waste": {
            "excess_stock": waste[
                "excess_stock"
            ],
            "waste_risk": waste[
                "waste_risk"
            ],
            "days_to_expiry": days_to_expiry,
            "recommendation": waste[
                "recommendation"
            ]
        }
    }
        # ----------------------------------------
    # 5. IBM Granite AI Recommendation
    # ----------------------------------------

    ai_recommendation = generate_ai_recommendation(result)

    result["ai_recommendation"] = ai_recommendation
    return result


# ----------------------------------------
# Test Complete AI Pipeline
# ----------------------------------------

if __name__ == "__main__":

    result = analyze_product(
        product="BEVERAGES",
        store=1,
        current_stock=1500,
        incoming_stock=300,
        safety_stock=200,
        days_to_expiry=3
    )

    print("\n==========================================")
    print("       FreshStock AI Analysis")
    print("==========================================")

    print(f"Product: {result['product']}")
    print(f"Store: {result['store']}")

    print("\n📈 DEMAND FORECAST")
    print(
        f"Predicted Demand: "
        f"{result['forecast']['predicted_demand']:.2f}"
    )

    print("\n📦 INVENTORY")
    print(
        f"Current Stock: "
        f"{result['inventory']['current_stock']}"
    )

    print(
        f"Incoming Stock: "
        f"{result['inventory']['incoming_stock']}"
    )

    print(
        f"Recommended Order: "
        f"{result['inventory']['recommended_order']:.2f}"
    )

    print(
        f"Stock-out Risk: "
        f"{result['inventory']['stockout_risk']}"
    )

    print("\n🗑️ WASTE RISK")

    print(
        f"Excess Stock: "
        f"{result['waste']['excess_stock']:.2f}"
    )

    print(
        f"Days To Expiry: "
        f"{result['waste']['days_to_expiry']}"
    )

    print(
        f"Waste Risk: "
        f"{result['waste']['waste_risk']}"
    )

    print(
        f"Recommendation: "
        f"{result['waste']['recommendation']}"
    )
    print("\n🤖 IBM GRANITE AI RECOMMENDATION")
    print("------------------------------------------")
    print(result["ai_recommendation"])
    print("------------------------------------------")
    print("\n==========================================")
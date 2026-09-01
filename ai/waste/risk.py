"""
FreshStock AI - Waste Risk Detection

Identifies inventory that may be at risk of becoming waste.
"""


def calculate_waste_risk(
    current_stock,
    predicted_demand,
    incoming_stock=0,
    days_to_expiry=7
):
    """
    Calculate waste risk based on inventory,
    expected demand and remaining shelf life.
    """

    total_available = current_stock + incoming_stock

    # Inventory remaining after expected demand
    excess_stock = max(
        0,
        total_available - predicted_demand
    )

    # Percentage of inventory that may remain unused
    if total_available > 0:
        excess_percentage = (
            excess_stock / total_available
        ) * 100
    else:
        excess_percentage = 0

    # --------------------------------------------------
    # Waste risk logic
    # --------------------------------------------------

    if days_to_expiry <= 1 and excess_stock > 0:
        risk = "CRITICAL"

    elif days_to_expiry <= 2 and excess_percentage >= 20:
        risk = "HIGH"

    elif days_to_expiry <= 5 and excess_percentage >= 20:
        risk = "MEDIUM"

    elif excess_percentage >= 40:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    # --------------------------------------------------
    # Recommendation
    # --------------------------------------------------

    if risk == "CRITICAL":
        recommendation = (
            "Use inventory immediately, prioritize older stock "
            "and avoid additional purchases."
        )

    elif risk == "HIGH":
        recommendation = (
            "Prioritize this inventory and reduce the next purchase."
        )

    elif risk == "MEDIUM":
        recommendation = (
            "Monitor inventory closely and consider reducing "
            "the next order."
        )

    else:
        recommendation = (
            "Inventory level is healthy. Continue normal monitoring."
        )

    return {
        "current_stock": round(current_stock, 2),
        "incoming_stock": round(incoming_stock, 2),
        "total_available": round(total_available, 2),
        "predicted_demand": round(predicted_demand, 2),
        "excess_stock": round(excess_stock, 2),
        "excess_percentage": round(excess_percentage, 2),
        "days_to_expiry": days_to_expiry,
        "waste_risk": risk,
        "recommendation": recommendation
    }


# --------------------------------------------------
# Test the module
# --------------------------------------------------

if __name__ == "__main__":

    result = calculate_waste_risk(
        current_stock=1500,
        predicted_demand=2114.01,
        incoming_stock=300,
        days_to_expiry=3
    )

    print("\n======================================")
    print("       FreshStock AI Waste Risk")
    print("======================================")

    print(f"Current Stock: {result['current_stock']}")
    print(f"Incoming Stock: {result['incoming_stock']}")
    print(f"Total Available: {result['total_available']}")
    print(f"Predicted Demand: {result['predicted_demand']}")

    print(f"\nExcess Stock: {result['excess_stock']}")
    print(f"Excess Percentage: {result['excess_percentage']}%")
    print(f"Days To Expiry: {result['days_to_expiry']}")

    print(f"\nWaste Risk: {result['waste_risk']}")

    print(
        f"Recommendation: "
        f"{result['recommendation']}"
    )

    print("======================================")
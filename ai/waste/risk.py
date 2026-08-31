"""
Waste risk analysis module for FreshStock AI.
"""

def calculate_waste_risk(
    current_stock,
    expected_demand,
    days_to_expiry
):
    """
    Calculate a simple waste risk level.
    """

    excess_stock = current_stock - expected_demand

    if days_to_expiry <= 1 and excess_stock > 0:
        return "High"

    if days_to_expiry <= 3 and excess_stock > 0:
        return "Medium"

    return "Low"

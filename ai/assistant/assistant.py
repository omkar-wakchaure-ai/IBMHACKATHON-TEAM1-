"""
FreshStock AI Assistant.

This module will combine inventory information
with IBM Granite to generate human-readable
warehouse recommendations.
"""

def build_inventory_context(
    product,
    current_stock,
    expected_demand,
    days_to_expiry,
    waste_risk
):
    return f"""
Product: {product}
Current Stock: {current_stock}
Expected Demand: {expected_demand}
Days to Expiry: {days_to_expiry}
Waste Risk: {waste_risk}
"""

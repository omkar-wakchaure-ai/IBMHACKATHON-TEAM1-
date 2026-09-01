"""
Inventory optimization module for FreshStock AI.
"""

def calculate_recommended_order(
    forecast_demand,
    current_stock,
    incoming_stock=0
):
    """
    Calculate a basic recommended order quantity.
    """

    available_stock = current_stock + incoming_stock

    recommended_order = forecast_demand - available_stock

    return max(0, recommended_order)

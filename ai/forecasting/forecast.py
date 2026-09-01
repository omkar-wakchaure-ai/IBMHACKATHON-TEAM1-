"""
Demand forecasting module for FreshStock AI.
"""

def forecast_demand(product, historical_demand):
    """
    Placeholder for the demand forecasting model.
    """

    if not historical_demand:
        return 0

    return sum(historical_demand) / len(historical_demand)

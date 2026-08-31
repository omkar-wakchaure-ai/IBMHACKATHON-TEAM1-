from datetime import date

def calculate_freshness(mfg_date: date, exp_date: date) -> float:
    total_shelf_life = (exp_date - mfg_date).days
    days_left = (exp_date - date.today()).days
    
    if total_shelf_life <= 0:
        return 0.0
    freshness = (days_left / total_shelf_life) * 100
    return max(0.0, min(100.0, freshness))

def calculate_spoilage_risk(current_stock: float, predicted_demand: float, days_to_expiry: int) -> str:
    if days_to_expiry <= 2 and current_stock > predicted_demand:
        return "HIGH"
    elif days_to_expiry <= 5:
        return "MEDIUM"
    return "LOW"
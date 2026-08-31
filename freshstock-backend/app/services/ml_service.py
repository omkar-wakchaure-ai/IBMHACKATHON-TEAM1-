import numpy as np
from datetime import datetime, timedelta

def get_demand_forecast(product_name: str, days: int = 7) -> dict:
    """
    Hackathon Mock: In a real app, this loads 'demand_model.pkl' to run predictions.
    Here it generates realistic looking variance for the frontend charts.
    """
    base_demand = 120 if product_name.lower() == 'tomatoes' else 60
    
    forecast = []
    for i in range(days):
        target_date = datetime.now() + timedelta(days=i)
        predicted = base_demand + np.random.randint(-15, 25)
        forecast.append({
            "date": target_date.strftime('%Y-%m-%d'),
            "predicted_demand": float(predicted)
        })
        
    recommended = sum(f['predicted_demand'] for f in forecast) * 1.15 # 15% safety stock buffer
        
    return {
        "product_name": product_name,
        "forecast": forecast,
        "recommended_order": float(recommended),
        "confidence_score": 92.4
    }
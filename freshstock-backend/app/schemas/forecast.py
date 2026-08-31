from pydantic import BaseModel
from typing import List

class DemandData(BaseModel):
    date: str
    predicted_demand: float

class ForecastResponse(BaseModel):
    product_name: str
    forecast: List[DemandData]
    recommended_order: float
    confidence_score: float
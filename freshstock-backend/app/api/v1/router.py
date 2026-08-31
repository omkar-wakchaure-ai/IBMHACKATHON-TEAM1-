from fastapi import APIRouter
from app.api.v1.endpoints import products

api_router = APIRouter()

# Link the product endpoints to the main router
api_router.include_router(products.router, prefix="/products", tags=["Ingestion Portal"])

# Placeholders for the rest of your hackathon endpoints
# api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
# api_router.include_router(whatsapp.router, prefix="/whatsapp", tags=["Supplier WhatsApp Alerts"])
# api_router.include_router(forecasting.router, prefix="/forecast", tags=["ML Predictions"])
from fastapi import APIRouter

from app.api.v1.endpoints.products import router as products_router
from app.api.v1.endpoints.analytics import router as analytics_router
from app.api.v1.endpoints.ai import router as ai_router


router = APIRouter()


@router.get("/health")
def api_health_check():
    return {
        "status": "healthy",
        "api_version": "v1",
    }


router.include_router(products_router)
router.include_router(analytics_router)
router.include_router(ai_router)
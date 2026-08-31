from fastapi import APIRouter

from app.api.v1.endpoints.products import router as products_router

router = APIRouter()


@router.get("/health")
def api_health_check():
    return {
        "status": "healthy",
        "api_version": "v1",
    }


router.include_router(products_router)
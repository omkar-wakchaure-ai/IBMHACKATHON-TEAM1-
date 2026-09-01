from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.ai_assistant_service import generate_assistant_response


router = APIRouter(
    prefix="/ai-assistant",
    tags=["AI Assistant"]
)


@router.get("/recommendation/{product_id}")
def assistant_recommendation(
    product_id: int,
    db: Session = Depends(get_db)
):
    result = generate_assistant_response(db, product_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return result
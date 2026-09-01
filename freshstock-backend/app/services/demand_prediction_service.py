from sqlalchemy.orm import Session
from app.models.product import Product as ProductModel


def predict_restock_need(db: Session):
    products = db.query(ProductModel).all()

    predictions = []

    for product in products:

        if product.quantity <= 10:
            recommendation = "RESTOCK URGENTLY"

        elif product.quantity <= 20:
            recommendation = "RESTOCK SOON"

        else:
            recommendation = "STOCK LEVEL OK"

        predictions.append({
            "product_id": product.id,
            "product_name": product.name,
            "current_quantity": product.quantity,
            "prediction": recommendation
        })

    return predictions
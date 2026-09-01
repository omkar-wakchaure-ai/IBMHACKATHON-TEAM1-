from app.models.product import Product as ProductModel


def calculate_inventory_risk(product):
    """
    Calculate inventory risk based on current stock,
    predicted demand, and expiry information.
    """

    quantity = product.quantity

    # Stock risk
    if quantity <= 5:
        stock_risk = "CRITICAL"
    elif quantity <= 10:
        stock_risk = "HIGH"
    elif quantity <= 20:
        stock_risk = "MEDIUM"
    else:
        stock_risk = "LOW"

    # Expiry risk
    expiry_risk = "LOW"

    if product.expiry_date is not None:
        from datetime import date

        days_remaining = (
            product.expiry_date - date.today()
        ).days

        if days_remaining < 0:
            expiry_risk = "CRITICAL"
        elif days_remaining <= 3:
            expiry_risk = "HIGH"
        elif days_remaining <= 7:
            expiry_risk = "MEDIUM"

    # Overall risk
    if "CRITICAL" in [stock_risk, expiry_risk]:
        overall_risk = "CRITICAL"

    elif "HIGH" in [stock_risk, expiry_risk]:
        overall_risk = "HIGH"

    elif "MEDIUM" in [stock_risk, expiry_risk]:
        overall_risk = "MEDIUM"

    else:
        overall_risk = "LOW"

    return {
        "product_id": product.id,
        "product_name": product.name,
        "category": product.category,
        "current_quantity": quantity,
        "stock_risk": stock_risk,
        "expiry_risk": expiry_risk,
        "overall_risk": overall_risk
    }


def generate_inventory_risk_report(db):

    products = db.query(ProductModel).all()

    risks = []

    for product in products:
        risks.append(
            calculate_inventory_risk(product)
        )

    return risks
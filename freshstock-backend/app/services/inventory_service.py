from datetime import date, timedelta

from sqlalchemy.orm import Session

from app.models.product import Product as ProductModel
from app.schemas.product import Product, ProductCreate


# ---------------------------------------------------------
# GET ALL PRODUCTS
# ---------------------------------------------------------

def get_all_products(db: Session) -> list[Product]:
    products = db.query(ProductModel).all()

    return [
        Product.model_validate(
            product,
            from_attributes=True
        )
        for product in products
    ]


# ---------------------------------------------------------
# GET SINGLE PRODUCT
# ---------------------------------------------------------

def get_product(
    db: Session,
    product_id: int
) -> Product | None:

    product = (
        db.query(ProductModel)
        .filter(ProductModel.id == product_id)
        .first()
    )

    if product is None:
        return None

    return Product.model_validate(
        product,
        from_attributes=True
    )


# ---------------------------------------------------------
# CREATE PRODUCT
# ---------------------------------------------------------

def create_product(
    db: Session,
    product_data: ProductCreate
) -> Product:

    product = ProductModel(
        name=product_data.name,
        category=product_data.category,
        quantity=product_data.quantity,
        expiry_date=product_data.expiry_date,
        supplier_id=product_data.supplier_id,
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return Product.model_validate(
        product,
        from_attributes=True
    )


# ---------------------------------------------------------
# UPDATE PRODUCT
# ---------------------------------------------------------

def update_product(
    db: Session,
    product_id: int,
    product_data: ProductCreate
) -> Product | None:

    product = (
        db.query(ProductModel)
        .filter(ProductModel.id == product_id)
        .first()
    )

    if product is None:
        return None

    product.name = product_data.name
    product.category = product_data.category
    product.quantity = product_data.quantity
    product.expiry_date = product_data.expiry_date
    product.supplier_id = product_data.supplier_id

    db.commit()
    db.refresh(product)

    return Product.model_validate(
        product,
        from_attributes=True
    )


# ---------------------------------------------------------
# DELETE PRODUCT
# ---------------------------------------------------------

def delete_product(
    db: Session,
    product_id: int
) -> bool:

    product = (
        db.query(ProductModel)
        .filter(ProductModel.id == product_id)
        .first()
    )

    if product is None:
        return False

    db.delete(product)
    db.commit()

    return True


# ---------------------------------------------------------
# LOW STOCK PRODUCTS
# ---------------------------------------------------------

def get_low_stock_products(
    db: Session,
    threshold: int = 10
) -> list[Product]:

    products = (
        db.query(ProductModel)
        .filter(ProductModel.quantity <= threshold)
        .all()
    )

    return [
        Product.model_validate(
            product,
            from_attributes=True
        )
        for product in products
    ]


# ---------------------------------------------------------
# EXPIRING PRODUCTS
# ---------------------------------------------------------

def get_expiring_products(
    db: Session,
    days: int = 7
) -> list[Product]:

    today = date.today()
    expiry_limit = today + timedelta(days=days)

    products = (
        db.query(ProductModel)
        .filter(
            ProductModel.expiry_date.isnot(None),
            ProductModel.expiry_date >= today,
            ProductModel.expiry_date <= expiry_limit,
        )
        .all()
    )

    return [
        Product.model_validate(
            product,
            from_attributes=True
        )
        for product in products
    ]
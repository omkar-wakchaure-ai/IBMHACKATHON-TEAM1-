from app.schemas.product import Product, ProductCreate


# Temporary in-memory storage.
# We will replace this with the project's database/data layer later.
_products: list[Product] = []

_next_id = 1


def get_all_products() -> list[Product]:
    return _products


def create_product(product_data: ProductCreate) -> Product:
    global _next_id

    product = Product(
        id=_next_id,
        **product_data.model_dump()
    )

    _products.append(product)
    _next_id += 1

    return product
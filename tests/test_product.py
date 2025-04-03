from src.product import Product


def test_prod(fixture_product: Product) -> None:
    """Тест"""
    assert fixture_product.name == "Samsung Galaxy C23 Ultra"
    assert fixture_product.description == "256GB, Серый цвет, 200MP камера"
    assert fixture_product.price == 180000.0
    assert fixture_product.quantity == 5

from src.category import Category
from src.product import Product


def test_prod(fixture_product: Product, fixture_category: Category) -> None:
    """Тест"""
    fixture_category.products = [fixture_product]
    assert fixture_category.name == "Смартфоны"
    assert fixture_category.description == "Смартфоны, как средство связи"
    assert fixture_category.products[0].price == 180000.0
    assert fixture_category.products[0].name == "Samsung Galaxy C23 Ultra"
    assert fixture_category.products[0].description == "256GB, Серый цвет, 200MP камера"
    assert fixture_category.products[0].quantity == 5
    assert fixture_category.category_count == 1
    assert fixture_category.product_count == 2

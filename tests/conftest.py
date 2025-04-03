import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def fixture_product() -> Product:
    """Фикстура продукт."""
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def fixture_category() -> Category:
    """Фикстура категории"""
    product_1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category("Смартфоны", "Смартфоны, как средство связи", [product_1, product_2])

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

    return Category("Смартфоны", "Смартфоны, как средство связи", [])

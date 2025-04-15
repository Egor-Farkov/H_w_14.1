import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def fixture_product() -> Product:
    """Фикстура продукт."""
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def fixture_category() -> Category:
    """Фикстура категории"""

    return Category("Смартфоны", "Смартфоны, как средство связи", [])


@pytest.fixture
def fixture_smartphone() -> Smartphone:
    """Фикстура для смартфона"""
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture()
def fixture_lawn_grass() -> LawnGrass:
    """Фикстура для газонной травы"""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

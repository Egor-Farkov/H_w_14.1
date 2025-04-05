from unittest.mock import patch

from _pytest.capture import CaptureFixture

from src.category import Category
from src.product import Product


def test_prod(fixture_product: Product, fixture_category: Category) -> None:
    """Тест."""
    fixture_category.add_product(fixture_product)
    assert fixture_category.name == "Смартфоны"
    assert fixture_category.description == "Смартфоны, как средство связи"
    assert fixture_category.products == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert fixture_category.category_count == 1
    assert fixture_category.product_count == 5


def test_quantity(fixture_product: Product, fixture_category: Category) -> None:
    """Тест"""
    fixture_category.add_product(fixture_product)
    fixture_product.quantity = 10
    fixture_category.add_product(fixture_product)
    assert fixture_category.product_count == 30


def test_low_price(capsys: CaptureFixture[str], fixture_product: Product, fixture_category: Category) -> None:
    """Тест"""
    with patch("builtins.input", lambda _: "y"):
        fixture_category.add_product(fixture_product)
        fixture_product.price = 10
        fixture_category.add_product(fixture_product)
        read_out = capsys.readouterr()
        assert read_out.out == ""

    with patch("builtins.input", lambda _: "n"):
        fixture_category.add_product(fixture_product)
        fixture_product.price = 10
        fixture_category.add_product(fixture_product)
        read_out = capsys.readouterr()
        assert read_out.out == ""


def test_up_price(capsys: CaptureFixture[str], fixture_product: Product, fixture_category: Category) -> None:
    """Тест"""
    with patch("builtins.input", lambda _: "y"):
        fixture_category.add_product(fixture_product)
        fixture_product.price = 1000000
        fixture_category.add_product(fixture_product)
        read_out = capsys.readouterr()
        assert read_out.out == ""

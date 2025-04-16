import pytest
from _pytest.capture import CaptureFixture

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


def test_prod(fixture_product: Product) -> None:
    """Тест."""
    assert fixture_product.name == "Samsung Galaxy C23 Ultra"
    assert fixture_product.description == "256GB, Серый цвет, 200MP камера"
    assert fixture_product.price == 180000.0
    assert fixture_product.quantity == 5


def test_change_price(capsys: CaptureFixture[str], fixture_product: Product) -> None:
    """Тест."""
    fixture_product.price = 0
    read_out = capsys.readouterr()
    assert read_out.out == (
        "Product(Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, "
        "5)\n"
        "Цена не должна быть нулевая или отрицательная\n"
    )


def test_new_product(fixture_product: Product) -> None:
    """Тест"""
    prod_dict = {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }

    data = Product.new_product(prod_dict)
    assert isinstance(data, Product)


def test_str_category() -> None:
    cls_prod = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    cls_cat = Category("Смартфоны", "Смартфоны, как средство связи", [cls_prod])
    assert str(cls_cat) == "Смартфоны, количество продуктов: 4 шт."
    assert str(cls_prod) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert cls_prod + cls_prod == 1800000.0


def test_add_prod(fixture_smartphone: Smartphone, fixture_lawn_grass: LawnGrass, fixture_category: Category) -> None:
    with pytest.raises(TypeError):
        fixture_smartphone + fixture_lawn_grass
    with pytest.raises(TypeError):
        fixture_category.add_product("Not a product")

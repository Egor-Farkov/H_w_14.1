from _pytest.capture import CaptureFixture

from src.product import Product


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
    assert read_out.out == "Цена не должна быть нулевая или отрицательная\n"


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

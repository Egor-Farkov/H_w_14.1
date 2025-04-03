from src.product import Product


class Category:
    """Класс по описанию категорий."""

    name: str
    description: str
    products: list[Product]

    # Переменная на уровне класса по подсчету количества категорий
    category_count = 0
    # Переменная на уровне класса по подсчету количества товаров
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Метод для инициализации экземпляра класса."""

        self.name = name
        self.description = description
        self.products = products

        self.category_count += 1
        self.product_count += len(products) if products else 0

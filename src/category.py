from src.product import Product


class Category:
    """Класс по описанию категорий."""

    name: str
    description: str
    __products: list[Product] = []

    # Переменная на уровне класса по подсчету количества категорий
    category_count = 0
    # Переменная на уровне класса по подсчету количества товаров
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Метод для инициализации экземпляра класса."""

        self.name = name
        self.description = description
        self.__products = products
        self.category_count += 1

    @classmethod
    def add_product(cls, product: Product) -> None:
        """Класс-метод для добавления продуктов"""
        for item in cls.__products:
            if item.name == product.name:
                item.quantity += product.quantity

                if item.price <= product.price:
                    item.price = product.price
                else:
                    answer_user = input("Согласны на понижение цены, если да, введите: y, если нет: n")

                    if answer_user.lower() == "y":
                        item.price = product.price
        cls.product_count += product.quantity
        cls.__products.append(product)

    @property
    def products(self) -> list:
        """Геттер"""
        list_products = []
        for product in Category.__products:
            list_products.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return list_products

    def __str__(self) -> str:
        """Возвращает строку: название категории, количество продуктов: X шт."""
        return f"{self.name}, количество продуктов: {self.product_count} шт."

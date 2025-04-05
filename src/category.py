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

    def __init__(self, name: str, description: str):
        """Метод для инициализации экземпляра класса."""

        self.name = name
        self.description = description

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
    def products(self) -> str:
        """Геттер"""
        list_products = []
        for product in self.__products:
            list_products.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(list_products)

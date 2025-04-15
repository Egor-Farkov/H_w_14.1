from typing import Any


class Product:
    """Создан клас продуктов."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса."""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_attr: dict) -> Any:
        """Класс-метод новых продуктов"""
        return Product(**dict_attr)

    @property
    def price(self) -> float:
        """Геттер"""
        return self.__price

    @price.setter
    def price(self, set_price: float) -> None:
        """Сеттер, который задает значения цены"""
        if set_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = set_price

    def __str__(self) -> str:
        """Возвращает строку: Название продукта, X руб. Остаток: X шт."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """Возвращает сумму произведений цены на количество у двух объектов."""
        if type(self) == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError("Ошибка сложения классов")


class Smartphone(Product):
    """Подкласс смартфон"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """Метод для инициализации экземпляра подкласса."""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Подкласс трава зеленая"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Метод для инициализации экземпляра подкласса."""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

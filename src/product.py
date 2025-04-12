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
        return self.__price * self.quantity + other.__price * other.quantity

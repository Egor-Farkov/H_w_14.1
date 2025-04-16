from abc import ABC, abstractmethod
from typing import Any

from src.product import Product


class BaseCategory(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def add_product(self, product: Any) -> None:
        pass


class Category(BaseCategory):
    """Класс по описанию категорий."""

    __slots__ = ("name", "description", "__products")

    name: str
    description: str

    # Переменная на уровне класса по подсчету количества категорий
    category_count = 0
    # Переменная на уровне класса по подсчету количества товаров
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Метод для инициализации экземпляра класса."""

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Any) -> None:
        """Класс-метод для добавления продуктов"""
        if not issubclass(product.__class__, Product):
            raise TypeError("Складывать можно только объекты Product и дочерние от них.")

        for item in self.__products:
            if item.name == product.name:
                item.quantity += product.quantity

                if item.price <= product.price:
                    item.price = product.price
                else:
                    answer_user = input("Согласны на понижение цены, если да, введите: y, если нет: n")

                    if answer_user.lower() == "y":
                        item.price = product.price
        self.product_count += product.quantity
        self.__products.append(product)

    @property
    def products(self) -> list:
        """Геттер"""
        list_products = []
        for product in self.__products:
            list_products.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return list_products

    def __str__(self) -> str:
        """Возвращает строку: название категории, количество продуктов: X шт."""
        return f"{self.name}, количество продуктов: {self.product_count} шт."

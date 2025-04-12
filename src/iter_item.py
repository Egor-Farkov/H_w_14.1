from typing import Any

from src.category import Category


class IterItem:
    """
    Класс принимает на вход объект класса категории и производит итерацию по товарам,
    которые хранятся в данной категории.
    :return очередной товар категории.
    """

    item: Category
    counter = 0

    def __init__(self, item: Any) -> None:
        """Инициализирует итератор"""
        self.item = item

    def __iter__(self) -> Any:
        """Возвращает итератор."""
        self.counter = 0
        return self

    def __next__(self) -> Any:
        """Итерация по продуктам"""
        if self.counter < len(self.item.products):
            ind_cnt = self.item.products[self.counter]
            self.counter += 1
            return ind_cnt
        else:
            raise StopIteration("Итерация окончена")

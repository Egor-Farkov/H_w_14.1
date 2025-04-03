from src.read_file_json import read_json_file


def test_read_json_file() -> None:
    """Тест чтения файла json"""
    data = read_json_file()
    assert data == [
        {
            "description": "Смартфоны, как средство не только коммуникации, но и "
            "получение дополнительных функций для удобства жизни",
            "name": "Смартфоны",
            "products": [
                {
                    "description": "256GB, Серый цвет, 200MP камера",
                    "name": "Samsung Galaxy C23 Ultra",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"description": "512GB, Gray space", "name": "Iphone 15", "price": 210000.0, "quantity": 8},
                {"description": "1024GB, Синий", "name": "Xiaomi Redmi Note 11", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "description": "Современный телевизор, который позволяет наслаждаться "
            "просмотром, станет вашим другом и помощником",
            "name": "Телевизоры",
            "products": [
                {"description": "Фоновая подсветка", "name": '55" QLED 4K', "price": 123000.0, "quantity": 7}
            ],
        },
    ]

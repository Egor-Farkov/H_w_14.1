from src.category import Category
from src.product import Product
from src.read_file_json import read_json_file

if __name__ == "__main__":

    data_list = read_json_file()

    # Цикл
    for data in data_list:  # смартфоны, телевизоры
        category_name = data["name"]
        category_description = data["description"]
        category_data = Category(category_name, category_description)
        products = data["products"]

        for product in products:
            product_name = product["name"]
            product_description = product["description"]
            product_price = product["price"]
            product_quantity = product["quantity"]
            product_cls = Product(
                name=product_name, description=product_description, price=product_price, quantity=product_quantity
            )

            category_data.add_product(product_cls)

    print(category_data.products, end="\n\n")


prod_dict = {
    "name": "Samsung Galaxy C23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 180000.0,
    "quantity": 5,
}
print(Product.new_product(prod_dict))

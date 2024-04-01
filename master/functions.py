import json
from master.classes import Category, Product


def load_products():  # pragma: no cover
    """
    Загружает данные из файла
    """
    with open('products.json', encoding='utf-8') as f:
        return json.load(f)


def get_category_full_list(load_products, full_list):
    """
    Возвращает полный список категорий с продуктами
    """
    for data in load_products:
        category = Category(name=data['name'], description=data['description'], products=[])
        for prod_data in data['products']:
            product = Product(**prod_data)
            category.products.append(product)
            full_list.append(category)
    return full_list

def get_product(name, description, price, quantity):
    new_prod = {}
    new_prod['name'] = name
    new_prod['description'] = description
    new_prod['price'] = price
    new_prod['quantity'] = quantity
    return new_prod

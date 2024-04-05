import json
from master.classes import Category, Product


def load_products():  # pragma: no cover
    """
    Загружает данные из файла
    """
    with open('products.json', encoding='utf-8') as f:
        return json.load(f)


def get_category_full_list(load_products):
    """
    Возвращает полный список категорий с продуктами
    """
    category_list = []
    for data in load_products:
        pr_list = []
        for prod_data in data['products']:
            product = Product(**prod_data)
            pr_list.append(product)
        category = Category(name=data['name'], description=data['description'], products=pr_list)
        category_list.append(category)
    return category_list

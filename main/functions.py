# импортировали функции
from classes import Category, Product
import json


# загрузили список категорий и продуктов
def load_products():
    """
    Загружает данные из файла
    """
    with open('products.json', 'r', encoding='utf-8') as f:
        file = f.read()
        products = json.loads(file)
    return products

# def get_product(products_info, index, product_index):
#     """
#     Фунция выводит данные для создания класса "Продукт"
#     """
#     for category in range(len(products_info)):


# def get_category(products_info, index):
#     """
#     Фунция выводит данные для создания класса "Категория"
#     """
#     for category_name in range(len(products_info)):
#         category = Category(
#             products_info[index]["name"],
#             products_info[index]["description"],
#             products_info[index]["products"])
#     index += 1
#     return f'Категория {category.name}\n{category.description}\nВключает: {category.products}\n'
#
#
#

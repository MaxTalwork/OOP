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

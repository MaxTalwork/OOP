import pytest
from main import functions, classes
from main.functions import get_category, load_products
from main.main import products_info

def test_get_category():
    assert functions.get_category(f'Категория {get_category.name}\n{get_category.description}\nВключает: {get_category.products}\n') == f'Категория Телевизоры\nСовременный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником\nВключает: [{"name": "55\" QLED 4K", "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}]'

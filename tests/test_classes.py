import pytest
from main import functions, classes
from main.classes import Category, Product


@pytest.fixture()
def category_tv():
    return Category('Телевизоры', 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником', [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ])


@pytest.fixture()
def product_sf():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)


def test_category(category_tv):
    assert category_tv.name == 'Телевизоры'
    assert category_tv.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником")
    assert category_tv.products == [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]


def test_product(product_sf):
    assert product_sf.name == "Samsung Galaxy C23 Ultra"
    assert product_sf.description == "256GB, Серый цвет, 200MP камера"
    assert product_sf.price == 180000.0
    assert product_sf.quantity == 5

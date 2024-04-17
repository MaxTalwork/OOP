import pytest
from master.classes.product import Product
from master.classes.category import Category


@pytest.fixture
def product_test1():
    return Product('a', 'aa', 10.0, 3)


@pytest.fixture
def category_test():
    return Category('a', 's', [Product('qq', 'ww', 10.0, 1)])


test_list = [{"name": "Телевизоры",
              "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
                             "станет вашим другом и помощником",
              "products": [{"name": "55\" QLED 4K",
                            "description": "Фоновая подсветка",
                            "price": 123000.0,
                            "quantity": 7}]}]


def test_get_new_category(category_test):
    test_cat = category_test
    assert test_cat.name, test_cat.description == Category('a', 's', [
        Product('qq', 'ww', 10.0, 1)])

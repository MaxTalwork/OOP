import pytest
from master.classes import Product, Category


@pytest.fixture
def product_test1():
    return Product('aaa', 'aaa', 0.0, 0)


def test_init_product(product_test1):
    assert product_test1.name == 'aaa'
    assert product_test1.description == 'aaa'
    assert product_test1.price == 0.0
    assert product_test1.quantity == 0


@pytest.fixture
def category_test():
    return Category('aaa', 'aaa', [
        {'name': 'aaa', 'description': 'aaa', 'price': 0.0, 'quantity': 0},
        {'name': 'bbb', 'description': 'aaa', 'price': 0.0, 'quantity': 0}])


def test_init_category(category_test):
    assert category_test.name == 'aaa'
    assert category_test.description == 'aaa'
    assert category_test.products == [
        {'name': 'aaa', 'description': 'aaa', 'price': 0.0, 'quantity': 0},
        {'name': 'bbb', 'description': 'aaa', 'price': 0.0, 'quantity': 0}]


def test_category_counter(category_test):
    assert Category.categories_counter == 1


def test_products_counter(category_test):
    assert Category.products_counter == 2

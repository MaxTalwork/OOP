import pytest
from master.classes import Product, Category


@pytest.fixture
def product_test1():
    return Product('a', 'aa', 0.0, 0)


def test_init_product(product_test1):
    assert product_test1.name == 'a'
    assert product_test1.description == 'aa'
    assert product_test1.price == 0.0
    assert product_test1.quantity == 0


@pytest.fixture
def category_test():
    return Category('a', 'aa', [
        {'name': 'a', 'description': 'aa', 'price': 0.0, 'quantity': 0},
        {'name': 'b', 'description': 'bb', 'price': 0.1, 'quantity': 1}])


def test_init_category(category_test):
    assert category_test.name == 'a'
    assert category_test.description == 'aa'
    assert category_test.products == [
        {'name': 'a', 'description': 'aa', 'price': 0.0, 'quantity': 0},
        {'name': 'b', 'description': 'bb', 'price': 0.1, 'quantity': 1}]


def test_category_counter(category_test):
    assert Category.categories_counter == 1


def test_products_counter(category_test):
    assert Category.products_counter == 2

import pytest
from master.classes import Product, Category


@pytest.fixture
def product_test1():
    return Product('a', 'aa', 0.0, 0)


def test_init_product(product_test1):
    assert product_test1


@pytest.fixture
def category_test():
    return Category('a', 'aa', [Product('a', 'aa', 0.0, 0)])


def test_init_category(category_test):
    assert category_test


def test_category_counter(category_test):
    assert Category.categories_counter == 1


def test_products_counter(category_test):
    assert Category.products_counter == 1

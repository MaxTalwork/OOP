import pytest
from master.classes.Category import Category
from tests.test_Product import product_test1


@pytest.fixture
def category_test(product_test1):
    return Category('a', 'aa', [product_test1])


def test_init_category(category_test, product_test1):
    assert category_test.name == 'a'
    assert category_test.description == 'aa'
    assert category_test.products_counter == 1
    # assert category_test.products_set == {product_test1}


def test_get_products(category_test, product_test1):
    test_cat = category_test
    assert test_cat.get_products == [str(product_test1)]


def test_category_counter(category_test):
    assert Category.categories_counter == 1


def test_products_counter(category_test):
    assert Category.products_counter == 1

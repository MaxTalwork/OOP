import pytest
from master.class_Category import Product, Category


@pytest.fixture
def product_test1():
    return Product('a', 'aa', 0.0, 0)


def test_init_product(product_test1):
    assert product_test1


def test_new_prod(product_test1):
    assert print(product_test1) == print('a', 'aa', 10.0, 0)


def test_get_price(product_test1):
    price = -3
    assert f'Введена некорректная цена: {price} руб!' == f'Введена некорректная цена: -3 руб!'

    price = 15
    assert f'Цена товара: {price}' == f'Цена товара: 15'



@pytest.fixture
def category_test():
    return Category('a', 'aa', [Product('a', 'aa', 0.0, 0)])


def test_init_category(category_test):
    assert category_test


def test_get_products(category_test):
    test_cat = category_test
    assert test_cat.get_products() == [f'a, 0.0 руб. Остаток: 0 шт.']


def test_category_counter(category_test):
    assert Category.categories_counter == 1


def test_products_counter(category_test):
    assert Category.products_counter == 1

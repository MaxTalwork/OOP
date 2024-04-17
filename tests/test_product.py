import pytest
from master.classes.product import Product


@pytest.fixture
def product_test1():
    return Product('a', 'aa', 10.0, 3)


def test_init_product(product_test1):
    assert product_test1.name == 'a'
    assert product_test1.description == 'aa'
    assert product_test1.price == 10.0
    assert product_test1.quantity == 3
    assert product_test1.full_cost == 30.0


def test_price(product_test1):
    product_test1.price = 10.0
    assert product_test1.price == 10

    product_test1.price = 15.0
    assert product_test1.price == 15.0

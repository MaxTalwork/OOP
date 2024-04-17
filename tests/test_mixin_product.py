import pytest
from master.classes.product import Product


@pytest.fixture
def mixin_product_test1():
    return Product('a', 'aa', 10.0, 3)


def test_init_product(mixin_product_test1):
    assert mixin_product_test1.name == 'a'
    assert mixin_product_test1.description == 'aa'
    assert mixin_product_test1.price == 10.0
    assert mixin_product_test1.quantity == 3

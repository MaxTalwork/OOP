import pytest
from master.classes.AbstractProduct import AbstractProduct


@pytest.fixture
def product_test1():
    return AbstractProduct('a', 'aa', 0.0, 0)

import pytest
from master.classes.smartphone import Smartphone


@pytest.fixture
def smartphone_test1():
    return Smartphone('a', 'aa', 10.0, 3, 'Q', "w", "r", "e")


def test_init_smartphone(smartphone_test1):
    assert smartphone_test1.name == 'a'
    assert smartphone_test1.description == 'aa'
    assert smartphone_test1.get_price == 10.0
    assert smartphone_test1.performance == "Q"
    assert smartphone_test1.model == 'w'
    assert smartphone_test1.amount_memory == 'r'
    assert smartphone_test1.color == 'e'

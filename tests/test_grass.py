import pytest
from master.classes.grass import Grass


@pytest.fixture
def grass_test1():
    return Grass('a', 'aa', 10.0, 3, 'Q', "w", "e")


def test_init_grass(grass_test1):
    assert grass_test1.name == 'a'
    assert grass_test1.description == 'aa'
    assert grass_test1.price == 10.0
    assert grass_test1.manufacturer_country == "Q"
    assert grass_test1.germination_period == 'w'
    assert grass_test1.color == 'e'

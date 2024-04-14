import pytest
from master.functions import get_category_full_list
from master import class_Category


@pytest.fixture
def product_test1():
    return classes.Product('qq', 'ww', 10.0, 0)


@pytest.fixture
def category_test():
    return classes.Category('a', 's', [classes.Product('qq', 'ww', 10.0, 1)])


test_list = [{"name": "Телевизоры",
              "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
                             "станет вашим другом и помощником",
              "products": [{"name": "55\" QLED 4K",
                            "description": "Фоновая подсветка",
                            "price": 123000.0,
                            "quantity": 7}]}]


def test_get_category_full_list(category_test):
    new_p = classes.Product('q', 'w', 3, 4)
    category_list = []
    for data in test_list:
        pr_list = []
        for prod_data in data['products']:
            product = classes.Product(**prod_data)
            pr_list.append(product)
        category = classes.Category(name=data['name'], description=data['description'], products=pr_list)
        category_list.append(category)
        add_new_prod_check = 'yes'
        if add_new_prod_check == 'yes':
            pr_list.append(new_p)
            category = classes.Category(name=data['name'], description=data['description'], products=pr_list)
            category_list.append(category)
    add_new_prod_cat = 'yes'
    if add_new_prod_cat == 'yes':
        new_cat_name, new_cat_dis, pr_list = "qqq", "www", pr_list
        category = classes.Category(new_cat_name, new_cat_dis, pr_list)
        category_list.append(category)
    assert len(category_list) == 3
    assert len(pr_list) == 2


def test_get_new_category(category_test):
    test_cat = category_test
    assert test_cat.name, test_cat.description == classes.Category('a', 's', [
        classes.Product('qq', 'ww', 10.0, 1)])

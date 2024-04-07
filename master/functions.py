import json
from master.classes import Category, Product


def load_products():  # pragma: no cover
    """
    Загружает данные из файла
    """
    with open('products.json', encoding='utf-8') as f:
        return json.load(f)


def get_category_full_list(all_products):
    """
    Возвращает полный список категорий с продуктами
    """
    category_list = []
    for data in all_products:
        pr_list = []
        for prod_data in data['products']:
            product = Product(**prod_data)
            pr_list.append(product)
        category = Category(name=data['name'], description=data['description'], products=pr_list)
        category_list.append(category)
        add_new_prod_check = input(f'Хотите добавить новый товар в категорию {category.name}?')
        if add_new_prod_check == 'yes':
            # for pr in pr_list:
            #     if pr['name'] in pr_list:
            #
            pr_list.append(add_new_prod(pr_list))
            category = Category(name=data['name'], description=data['description'], products=pr_list)
            category_list.append(category)
    add_new_prod_cat = input(f'Хотите добавить новую категорию и товар в неё?')
    if add_new_prod_cat == 'yes':
        pr_list = []
        new_cat_name, new_cat_dis, pr_list = get_new_category(pr_list)
        category = Category(new_cat_name, new_cat_dis, pr_list)
        category_list.append(category)
    return category_list


def add_new_prod(pr_list):
    new_p = Product.new_prod(
        name=input('Название товара: '),
        description=input('Описание товара: '),
        price=float(input('Цена товара: ')),
        quantity=int(input('Количество товара: ')))
    return new_p


def get_new_category(pr_list):
    new_cat_name = input('Название категории: ')
    new_cat_dis = input('Описание категории: ')
    new_p = Product.new_prod(
        name=input('Название товара: '),
        description=input('Описание товара: '),
        price=float(input('Цена товара: ')),
        quantity=int(input('Количество товара: ')))
    pr_list.append(new_p)
    return new_cat_name, new_cat_dis, pr_list


def getter_pr(function):
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        print('result =', result)
        return result

    return inner

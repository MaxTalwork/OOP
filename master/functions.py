import json
from master.classes.Category import Category
from master.classes.Product import Product


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
        add_new_prod_check = input(f"Хотите добавить новый товар в категорию {category.name}?"
                                   f"\nВведите \"yes\" для подтверждения: ")
        if add_new_prod_check == 'yes':
            pr_list.append(add_new_prod())
            category = Category(name=data['name'], description=data['description'], products=pr_list)
            category_list.append(category)
    add_new_prod_cat = input(f'Хотите добавить новую категорию и товар в неё?\nВведите "yes" для подтверждения: ')
    if add_new_prod_cat == 'yes':
        pr_list = []
        new_pr = add_new_prod()
        pr_list.append(new_pr)
        new_cat_name, new_cat_dis = get_new_category()
        category = Category(new_cat_name, new_cat_dis, pr_list)
        category_list.append(category)
    return category_list


def add_new_prod():
    new_p = Product.new_prod(name=input('Название товара: '),
                             description=input('Описание товара: '),
                             price=float(input('Цена товара: ')),
                             quantity=int(input('Количество товара: ')))
    return new_p


def get_new_category():
    new_cat_name = input('Название категории: ')
    new_cat_dis = input('Описание категории: ')
    return new_cat_name, new_cat_dis

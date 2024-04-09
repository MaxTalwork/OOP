from master.functions import load_products, get_category_full_list
from master.classes import Category, Product, CategoryIter

loaded_products = load_products()
category_list = get_category_full_list(loaded_products)

for category in category_list:
    print(category.name, category.description, category.get_products)
    print(category)
    print(f'Общее количество категорий: {Category.categories_counter}')
    print(f'Общее количество уникальных продуктов: {Category.products_counter}')


prod_1 = Product('qq', 'ww', 5, 1)
prod_2 = Product('aa', 'sss', 23, 4)
print(prod_1)
print(prod_1.get_price)
prod_1.get_price = 15
print(prod_1.get_price)
print(prod_1+prod_2)

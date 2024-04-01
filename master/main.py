from master.functions import load_products, get_category_full_list
from master.classes import Category

loaded_products = load_products()
full_list: list[Category] = []
index = 0

category_list = get_category_full_list(loaded_products, full_list)

for ex in category_list:
    print(Category.products_set)
    print(f'Общее количество категорий: {Category.categories_counter}')
    print(f'Общее количество уникальных продуктов: {Category.products_counter}')
    index += 1

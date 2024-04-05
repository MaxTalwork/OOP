from master.functions import load_products, get_category_full_list
from master.classes import Category

loaded_products = load_products()
full_list = []
index = 0

category_list = get_category_full_list(loaded_products, full_list)

for cat in category_list:
    cat_name = cat.products
    print(cat_name)
    print(f'Общее количество категорий: {Category.categories_counter}')
    print(f'Общее количество уникальных продуктов: {Category.products_counter}')


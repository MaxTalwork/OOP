from master.functions import load_products, get_category_full_list
from master.classes import Category, Product

loaded_products = load_products()
category_loaded_list = get_category_full_list(loaded_products)
# added_categories = get_new_category()


category_list = category_loaded_list


for category in category_list:
    print(category.name, category.description, category.get_products())
    print(f'Общее количество категорий: {Category.categories_counter}')
    print(f'Общее количество уникальных продуктов: {Category.products_counter}')

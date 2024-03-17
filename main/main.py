# импортировали функции
from functions import load_products, get_category, get_product
from classes import Category


products_info = load_products()
index = 0
product_index = 0

# создали экземпляры класса "Категория" и "Продукт"
ex1 = get_category(products_info, 0)
ex2 = get_category(products_info, 1)

exp1 = get_product(products_info, 0, 1)
exp2 = get_product(products_info, 1, 0)

print(ex1)
print(ex2)

print(exp1)
print(exp2)

print(f'Общее количество категорий: {Category.categories_counter}')
print(f'Общее количество уникальных продуктов: {Category.products_counter}')

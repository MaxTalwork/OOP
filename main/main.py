# импортировали функции
from functions import load_products
from classes import Category, Product


products_info = load_products()
index = 0
product_index = 0

prod_name = "aaa"
prod_description = "aaa"
prod_price = 0.0
prod_quantity = 0


# print(products_info)
# создали экземпляры класса "Категория" и "Продукт"
product = Product(prod_name, prod_description, prod_price, prod_quantity)
prod_list = [product.get_product()]
category = Category('products_info', 'sdaad', prod_list)
print(category)

print(prod_list)

print(f'Общее количество категорий: {Category.categories_counter}')
print(f'Общее количество уникальных продуктов: {Category.products_counter}')

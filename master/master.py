# импортировали функции
import emp
from poetry.console.commands import self

from functions import load_products
from classes import Category, Product

# loaded_products = load_products()
# index = 0
# product_index = 0
# full_list = []

# for index in range(len(loaded_products)):
#     full_dic = {'category_name': loaded_products[index]['name'],
#                 'category_description': loaded_products[index]['description']}
#     category_products = loaded_products[index]['products']
#     for product_index in range(len(category_products)):
#         full_dic['prod_n'] = category_products[product_index]['name']
#         full_dic['prod_dis'] = category_products[product_index]['description']
#         full_dic['prod_price'] = category_products[product_index]['price']
#         full_dic['prod_quantity'] = category_products[product_index]['quantity']
#
#         full_list.extend(full_dic)
#         product_index += 1
#     index += 1
#     print(full_dic)

name = "a"
name2 = "aa"
name3 = "aab"
description = "b"
price = 0.0
quantity = 1
quantity2 = 2

category_name = "ca"
category_description = "cb"
category_prod = []


# создали экземпляры класса "Категория" и "Продукт"
product = Product(name, description, price, quantity)
product1 = Product(name2, description, price, quantity)
product2 = Product(name3, description, price, quantity)

print(product2.name, product2.description, product2.price, product2.quantity)
product_list = [Product.get_product(product), Product.get_product(product1)]
category = Category(category_name, category_description, product_list)
print(category)

# Category.add_products(category, product1)

# # print(prod_list)
#
# print(f'Общее количество категорий: {Category.categories_counter}')
# print(f'Общее количество уникальных продуктов: {Category.products_counter}')

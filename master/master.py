# импортировали функции


from functions import load_products
from classes import Category, Product

loaded_products = load_products()
# print(loaded_products)
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

# создали экземпляры класса "Категория" и "Продукт"
product1 = Product(loaded_products[0]['products'][0]['name'],
                   loaded_products[0]['products'][0]['description'],
                   loaded_products[0]['products'][0]['price'],
                   loaded_products[0]['products'][0]['quantity'])

product2 = Product(loaded_products[0]['products'][1]['name'],
                   loaded_products[0]['products'][1]['description'],
                   loaded_products[0]['products'][1]['price'],
                   loaded_products[0]['products'][1]['quantity'])

product3 = Product(loaded_products[0]['products'][2]['name'],
                   loaded_products[0]['products'][2]['description'],
                   loaded_products[0]['products'][2]['price'],
                   loaded_products[0]['products'][2]['quantity'])

product4 = Product(loaded_products[1]['products'][0]['name'],
                   loaded_products[1]['products'][0]['description'],
                   loaded_products[1]['products'][0]['price'],
                   loaded_products[1]['products'][0]['quantity'])

# print(product1.name, product1.description, product1.price, product1.quantity)
# print(product2.name, product2.description, product2.price, product2.quantity)
# print(product3.name, product3.description, product3.price, product3.quantity)
# print(product4.name, product4.description, product4.price, product4.quantity)

product_list1 = [Product.get_product(product1),
                 Product.get_product(product2),
                 Product.get_product(product3)]

product_list2 = [Product.get_product(product4)]

category1 = Category(loaded_products[0]['name'],
                     loaded_products[0]['description'],
                     product_list1)

category2 = Category(loaded_products[1]['name'],
                     loaded_products[1]['description'],
                     product_list2)

print(category1.name, category1.description, category1.products)
print(category2.name, category2.description, category2.products)

print(f'Общее количество категорий: {Category.categories_counter}')
print(f'Общее количество уникальных продуктов: {Category.products_counter}')

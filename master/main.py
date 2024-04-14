from master.functions import load_products, get_category_full_list
from master.class_Product import Product
from master.class_Category import Category
from master.class_Smartphone import Smartphone
from master.class_Grass import Grass

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

sm1 = Smartphone('aa', 'qq', 212, 21, 1112, 3334, 16, 'green')
sm2 = Smartphone('aa2', 'qq', 212, 10, 1112, 3334, 16, 'green')
print(sm1)
gr1 = Grass('pp', 'ooo', 122, 456, 'rtetret', 'fyftfy', 'ttuu')
print(gr1)
print(sm1+sm2)
print(sm1+gr1)


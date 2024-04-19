from master.functions import load_products, get_category_full_list
from master.classes.product import Product
from master.classes.category import Category, CategoryIter
from master.classes.smartphone import Smartphone
from master.classes.grass import Grass

loaded_products = load_products()
category_list = get_category_full_list(loaded_products)

for category in category_list:
    print(category.average_price())
    category_iterator = CategoryIter(category)
    for product in category_iterator:
        print(product)
        print(f'Общее количество категорий: {Category.categories_counter}')
        print(f'Общее количество уникальных продуктов: {Category.products_counter}')

cat = Category('qw', 'qwe',[])
print(cat.average_price())
# prod_1 = Product.new_prod('qq', 'ww', 5, 1)
# prod_2 = Product.new_prod('aa', 'sss', 23, 4)
# print(prod_1)
# print(prod_1.price)
# prod_1.price = 15
# print(prod_1.price)
# print(prod_1+prod_2)
#
# sm1 = Smartphone.new_prod('aa', 'qq', 212, 21, 1112, 3334, 16, 'green')
# sm2 = Smartphone.new_prod('aa2', 'qq', 212, 10, 1112, 3334, 16, 'green')
# print(sm1)
# gr1 = Grass.new_prod('pp', 'ooo', 122, 456, 'rtetret', 'fyftfy', 'ttuu')
# print(gr1)
# print(sm1+sm2)
# print(sm1+gr1)


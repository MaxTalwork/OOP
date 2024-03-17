# создаём классы Категория и Продукт.
# Для класса Категория вводим счётчик числа категорий и уникальных продуктов
class Category:

    name: str
    description: str
    products: list
    categories_set: set
    categories_counter: int
    products_set: set
    products_counter: int

    categories_set = set()
    categories_counter = 0
    products_set = set()
    products_counter = 0

    def __init__(self, name, description, products):

        self.name = name
        self.description = description
        self.products = products

        Category.categories_set.add(self.name)
        Category.categories_counter = len(Category.categories_set)

        products_names = []
        index = 0
        for products_name in range(len(self.products)):
            products_name = self.products[index]
            products_names.append(products_name['name'])
            index += 1
        products_set = set(products_names)

        Category.products_set.update(products_set)
        Category.products_counter = len(Category.products_set)

    # def __repr__(self):
    #     return f"{self.name}, {self.description}, {self.products}"


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    # def __repr__(self):
    #     return f"{self.name}, {self.description}, {self.price}, {self.quantity}"

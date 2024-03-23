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

    # def add_products(self):
    #     """ принимает на вход объект товара и добавляет его в список """
    #     new_product = {}
    #     new_product["name"] = input("Название товара: ")
    #     new_product["description"] = input("Описание товара: ")
    #     new_product["price"] = input("Цена товара: ")
    #     new_product["quantity"] = input("Количество товара: ")
    #     self.products.insert(new_product)
    #
        products_names = []
        index = 0
        for products_name in range(len(self.products)):
            products_name = self.products[index]
            products_names.append(products_name['name'])
            index += 1
        products_set = set(products_names)

        Category.products_set.update(products_set)
        Category.products_counter = len(Category.products_set)

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.products}"


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

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"

    def get_product(self):
        """Метод, который возвращает продукт ."""
        prod_dic = {}
        prod_dic['name'] = self.name
        prod_dic['description'] = self.description
        prod_dic['price'] = self.price
        prod_dic['quantity'] = self.quantity
        return prod_dic


    def __repr__(self):
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"

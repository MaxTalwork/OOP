# создаём классы Категория и Продукт.
# Для класса Категория вводим счётчик числа категорий и уникальных продуктов
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

    def get_product(self):
        """Метод, который возвращает продукт ."""
        prod_dic = {'name': self.name, 'description': self.description, 'price': self.price, 'quantity': self.quantity}
        return prod_dic

    # def __repr__(self):
    #     return f"{self.name}, {self.description}, {self.price}, {self.quantity}"


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
        self.__products = products

        Category.categories_set.add(self.name)
        Category.categories_counter = len(Category.categories_set)

    # def add_products(self, new_prod):
    #     """ принимает на вход объект товара и добавляет его в список """
    #     self.__products.insert(0, new_prod)
    #
        unic_products = []
    #     index = 0
    #     for products_name in range(len(self.__products)):
    #         products_name = self.__products[index]
    #         unic_products.append(products_name['name'])
    #         index += 1
        products_set = set(unic_products)

        Category.products_set.update(products_set)
        Category.products_counter = len(Category.products_set)

    # def __repr__(self):
    #     return f"{self.name}, {self.description}, {self.__products}"

# print(emp.Category__products)
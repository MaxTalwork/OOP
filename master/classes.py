class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    # def get_product(self):
    #     """Метод, который возвращает продукт ."""
    #     prod_dic = {'name': self.name,
    #                 'description': self.description,
    #                 'price': self.price,
    #                 'quantity': self.quantity}
    #     return prod_dic

    def __repr__(self):
        return f"!{self.name}, {self.description}, {self.price}, {self.quantity}!"


class Category:
    categories_set = set()
    categories_counter = 0
    products_set = set()
    products_counter = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        for data in self.products:
            Category.products_set.add(data)

        Category.categories_set.add(self.name)
        Category.categories_counter = len(Category.categories_set)

        Category.products_counter = len(Category.products_set)

    # def get_product(function):
    #     def inner(*args, **kwargs):
    #         result = function(*args, **kwargs)
    #         print('result =', result)
    #         return result
    #     return inner

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.products}"

class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"


class Category:
    categories_set = set()
    categories_counter = 0
    products_set = set()
    products_counter = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.categories_set.add(self.name)
        Category.categories_counter = len(Category.categories_set)

        for x in products:
            Category.products_set.add(x.name)
        Category.products_counter = len(Category.products_set)

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.products}"

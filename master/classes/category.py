from master.classes.product import Product


class Category:
    categories_set = set()
    categories_counter = 0
    products_set = set()
    products_counter = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        self.full_cost = 0
        self.prod_number = 0

        Category.categories_set.add(self.name)
        Category.categories_counter = len(Category.categories_set)

        for x in self.__products:
            Category.products_set.add(x.name)
        Category.products_counter = len(Category.products_set)

    @property
    def products_new_format(self):
        prod_list_format = []
        for prod in self.__products:
            prod_list_format.append(str(prod))
        return prod_list_format

    # def __repr__(self):
    #     return f"{self.name}, {self.description}, {self.__products}"

    def __len__(self):
        return len(self.__products)

    def __add__(self, other):
        for p in self.__products:
            if isinstance(p, Product) is False:
                return f'Объект в списке продуктов не относится к классу продуктов'

    def average_price(self):
        for p in self.__products:
            self.full_cost += p.price
            self.prod_number += 1
        try:
            average_price = self.full_cost / self.prod_number
        except ZeroDivisionError:
            average_price = 0
            return average_price
        return average_price

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)}"


class CategoryIter:
    def __init__(self, category):
        self.category_name = category.name
        self.category_description = category.description
        self.category_products = category.products_new_format

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.category_products) > 0:
            # cat_name = self.category_name
            # cat_description = self.category_description
            product = self.category_products.pop(0)
            return product
        else:
            raise StopIteration()

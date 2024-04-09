class Product:
    all_products = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.full_cost = self.price * self.quantity

        Product.all_products.append(dict(name=self.name,
                                         description=self.description,
                                         price=self.price,
                                         quantity=self.quantity))

    @classmethod
    def new_prod(cls, name, description, price, quantity):
        new_prod_name = name
        new_prod_description = description
        new_prod_price = price
        new_prod_quantity = quantity
        return cls(new_prod_name, new_prod_description, new_prod_price, new_prod_quantity)

    @property
    def get_price(self):
        if self.price <= 0:
            return f'Введена некорректная цена: {self.price} руб!'
        else:
            return f'Цена товара: {self.price}'

    @get_price.setter
    def get_price(self, new_price):
        if new_price < self.price:
            answer = input('Вы уверены, что хотите снизить цену на товар?\nВведите "y" для подтверждения ')
            if answer == 'y':
                self.price = new_price
        else:
            print('Установлена новая цена!')
            self.price = new_price

    @get_price.deleter
    def get_price(self):
        print('Delete price!')
        self.price = None

    def __add__(self, other):
        return self.full_cost + other.full_cost

    # def __repr__(self):
    #     return f"{self.name}, {self.description}, {self.price}, {self.quantity}"

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    categories_set = set()
    categories_counter = 0
    products_set = set()
    products_counter = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.categories_set.add(self.name)
        Category.categories_counter = len(Category.categories_set)

        for x in self.__products:
            Category.products_set.add(x)
        Category.products_counter = len(Category.products_set)

    @property
    def get_products(self):
        prod_list_format = []
        for prod in self.__products:
            prod_list_format.append(prod)
            # prod_list_format.append(f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.')
        return prod_list_format

    # def __repr__(self):
    #     return f"{self.name}, {self.description}, {self.__products}"

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)}"


class CategoryIter:
    def __init__(self, category):
        self.category = category

    def __iter__(self):
        return self

    def __next__(self):
        pr_list = []
        for pr in self.category.get_products:
            pr_list.append(pr)
        return pr_list

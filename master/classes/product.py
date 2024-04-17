from master.classes.abstract_product import AbstractProduct
from master.classes.mixin_product import MixinProduct


class Product(AbstractProduct, MixinProduct):
    all_products = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.full_cost = self.__price * self.quantity

        Product.all_products.append(self)

    @classmethod
    def new_prod(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def get_price(self, new_price):
        if self.__price <= 0:
            self.__price = f'Введена некорректная цена: {self.__price} руб!'
        elif new_price < self.__price:
            answer = input('Вы уверены, что хотите снизить цену на товар?\nВведите "y" для подтверждения ')
            if answer == 'y':
                self.__price = new_price
                if self.__price <= 0:
                    self.__price = f'Введена некорректная цена: {self.__price} руб!'
        else:
            print('Установлена новая цена!')
            self.__price = new_price

    @get_price.deleter
    def get_price(self):
        print('Delete price!')
        self.__price = None

    def __add__(self, other):
        if type(self) is type(other):
            return self.full_cost + other.full_cost
        else:
            return f'Ошибка, это разные классы продуктов'

    # def __repr__(self):
    #     return f"{self.name}, {self.description}, {self.__price}, {self.quantity}"

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."
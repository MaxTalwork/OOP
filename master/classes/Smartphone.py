from master.classes.Product import Product
from master.classes.MixinProduct import MixinProduct


class Smartphone(Product, MixinProduct):

    def __init__(self, name, description, get_price, quantity, performance, model, amount_memory, color):
        super().__init__(name, description, get_price, quantity)
        self.performance = performance
        self.model = model
        self.amount_memory = amount_memory
        self.color = color

    def __str__(self):
        return (f"{self.name}, {self.description}, {self.get_price},"
                f"{self.quantity}, {self.performance}, {self.model},"
                f"{self.amount_memory}, {self.color}")


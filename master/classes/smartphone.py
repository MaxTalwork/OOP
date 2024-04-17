from master.classes.product import Product


class Smartphone(Product):

    def __init__(self, name, description, get_price, quantity, performance, model, amount_memory, color):
        self.performance = performance
        self.model = model
        self.amount_memory = amount_memory
        self.color = color
        super().__init__(name, description, get_price, quantity)

    def __str__(self):
        return (f"{self.name}, {self.description}, {self.price},"
                f"{self.quantity}, {self.performance}, {self.model},"
                f"{self.amount_memory}, {self.color}")


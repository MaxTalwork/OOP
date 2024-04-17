class MixinProduct:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__()
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):  # pragma: no cover
        return f'Был добавлен продукт {self.name}, {self.description}, {self.price}, {self.quantity}'

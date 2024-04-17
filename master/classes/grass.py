from master.classes.product import Product
from master.classes.mixin_product import MixinProduct


class Grass(Product, MixinProduct):
    def __init__(self, name, description, price, quantity, manufacturer_country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color

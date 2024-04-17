class MixinProduct:

    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):  # pragma: no cover
        return f'Был добавлен продукт {self.__class__.__name__}, {tuple(self.__dict__.values())}'

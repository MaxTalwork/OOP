class MyException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка'

    def __str__(self):
        return self.message


class ShellEmpty(MyException):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Нет данных!'


class ShebangEmpty(MyException):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Шебанг!'


class ZeroValueError(MyException):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Кол-во товара равно 0!'


class ShellException(MyException):
    def __init__(self, content):
        if not content:
            raise ShellEmpty()
        elif content[0:2] != '#!':
            raise ShebangEmpty()
        else:
            self.eval()

    def eval(self):
        pass

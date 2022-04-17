"""
2. Дескрипторы с проверками типов и значений данных (+тесты)
"""


class IntegerDescriptor:
    """Класс-дескриптор для int"""
    def __init__(self, name):
        self.name = name
        self.num = 0

    def __get__(self, instance, owner):
        return self.num

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.num = value
        else:
            raise Exception("Not integer!")

    def __delete__(self, instance):
        self.num = 0


class StringDescriptor:
    """Класс-дескриптор для str"""
    def __init__(self, name):
        self.name = name
        self.string = "None"

    def __get__(self, instance, owner):
        return self.string

    def __set__(self, instance, value):
        if isinstance(value, str):
            self.string = value
        else:
            raise Exception("Not string!")

    def __delete__(self, instance):
        self.string = "None"


class PositiveIntegerDescriptor:
    """Класс-дескриптор для positive int"""
    def __init__(self, name):
        self.name = name
        self.positive_num = 1

    def __get__(self, instance, owner):
        return self.positive_num

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise Exception("Not positive integer!")

        self.positive_num = value

    def __delete__(self, instance):
        self.positive_num = 1


class Data:
    """Класс Data, содержащий дескрипторы"""
    rating = IntegerDescriptor('rating')
    name = StringDescriptor('name')
    price = PositiveIntegerDescriptor('price')

    def __str__(self):
        """Метод печати полей класса"""
        return (f"rating = {self.rating}\n"
                f"name = {self.name}\n"
                f"price = {self.price}\n")

    def delete_data(self):
        """Метод установки значений по умолчанию полей класса"""
        del self.rating
        del self.name
        del self.price


if __name__ == "__main__":
    pass

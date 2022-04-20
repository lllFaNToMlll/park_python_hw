"""
Домашнее задание #4
1. Написать метакласс, который в начале названий всех атрибутов
и методов (кроме магических) добавляет префикс "custom_" (+тесты).
"""


class CustomMeta(type):
    """Метакласс, который изменяет название всех атрибутов и методов
    (кроме магических) с добавлением "custom_" """
    def __new__(cls, name, bases, dct):
        res_dict = {}
        for atr_name, atr_value in dct.items():
            if not (atr_name.startswith('__') and atr_name.endswith("__")):
                res_dict["custom_" + atr_name] = atr_value
            else:
                res_dict[atr_name] = atr_value
        res_dict["__setattr__"] = cls.__setattr__
        print(res_dict)
        return super().__new__(cls, name, bases, res_dict)

    def __setattr__(cls, key, value):
        if not key.startswith("custom_"):
            cls.__dict__["custom_" + key] = value


class CustomClass(metaclass=CustomMeta):
    """Класс для проверки работы метакласса"""
    x = 50
    buf__ = 2
    def __init__(self, val=99):
        """Переопределение метода __init__"""
        self.val = val

    def line(self):
        """Метод, возвращающий х"""
        return 50

    def __str__(self):
        """Переопределение метода __str__"""
        return "Custom_by_metaclass"


if __name__ == "__main__":
    # inst = CustomClass()
    # print(inst.__dir__())
    # inst.custom_x
    # inst.custom_val
    # inst.custom_get_val()
    # inst.custom_line()
    # CustomClass.custom_x
    # print(str(inst))
    pass

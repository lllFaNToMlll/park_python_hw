"""
Реализовать класс, отнаследованный от списка
При этом один список:
Можно вычитать из другого
CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]) = CustomList([4, -1, -4, 7]);
Можно складывать с другим
CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]) = CustomList([6, 3, 10, 7]);
Результатом сложения/вычитания должен быть новый кастомный список;
Сложение/вычитание также должно работать с обычными списками:
[1, 2] +- CustomList([3, 4]) -> CustomList(...)
CustomList([3, 4]) +- [1, 2] -> CustomList(...)
При неравной длине, дополнять меньший список нулями только на время
выполнения операции. Исходные списки не должны изменяться;
При сравнении списков должна сравниваться сумма элементов списков;
Должен быть переопределен str, чтобы выводились элементы списка и их сумма;
Списки можно считать всегда числовыми;
На все должны быть тесты в отдельном модуле;
Перед отправкой на проверку код должен быть прогнан через flake8 и pylint;
"""


class CustomList(list):
    """Класс, отнаследованный от списка"""
    def __lt__(self, other):
        """Перегрузка оператора =="""
        sum_of_self = 0
        sum_of_other = 0
        len_first, len_second = len(self), len(other)
        if len_first > len_second:
            dif_of_len = len_first - len_second
            for index in range(len_second):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_self += self[index + len_second]
        elif len_second > len_first:
            dif_of_len = len_second - len_first
            for index in range(len_first):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_other += other[index + len_first]

        return sum_of_self < sum_of_other

    def __le__(self, other):
        """Перегрузка оператора =="""
        sum_of_self = 0
        sum_of_other = 0
        len_first, len_second = len(self), len(other)
        if len_first > len_second:
            dif_of_len = len_first - len_second
            for index in range(len_second):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_self += self[index + len_second]
        elif len_second > len_first:
            dif_of_len = len_second - len_first
            for index in range(len_first):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_other += other[index + len_first]

        return sum_of_self <= sum_of_other

    def __eq__(self, other):
        """Перегрузка оператора =="""
        sum_of_self = 0
        sum_of_other = 0
        len_first, len_second = len(self), len(other)
        if len_first > len_second:
            dif_of_len = len_first - len_second
            for index in range(len_second):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_self += self[index + len_second]
        elif len_second > len_first:
            dif_of_len = len_second - len_first
            for index in range(len_first):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_other += other[index + len_first]

        return sum_of_self == sum_of_other

    def __ne__(self, other):
        """Перегрузка оператора =="""
        sum_of_self = 0
        sum_of_other = 0
        len_first, len_second = len(self), len(other)
        if len_first > len_second:
            dif_of_len = len_first - len_second
            for index in range(len_second):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_self += self[index + len_second]
        elif len_second > len_first:
            dif_of_len = len_second - len_first
            for index in range(len_first):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_other += other[index + len_first]

        return sum_of_self != sum_of_other

    def __gt__(self, other):
        """Перегрузка оператора =="""
        sum_of_self = 0
        sum_of_other = 0
        len_first, len_second = len(self), len(other)
        if len_first > len_second:
            dif_of_len = len_first - len_second
            for index in range(len_second):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_self += self[index + len_second]
        elif len_second > len_first:
            dif_of_len = len_second - len_first
            for index in range(len_first):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_other += other[index + len_first]

        return sum_of_self > sum_of_other

    def __ge__(self, other):
        """Перегрузка оператора =="""
        sum_of_self = 0
        sum_of_other = 0
        len_first, len_second = len(self), len(other)
        if len_first > len_second:
            dif_of_len = len_first - len_second
            for index in range(len_second):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_self += self[index + len_second]
        elif len_second > len_first:
            dif_of_len = len_second - len_first
            for index in range(len_first):
                sum_of_self += self[index]
                sum_of_other += other[index]
            for index in range(dif_of_len):
                sum_of_other += other[index + len_first]

        return sum_of_self >= sum_of_other

    def __add__(self, other):
        """Перегрузка оператора сложения"""
        list_of_sum = []
        len_first, len_second = len(self), len(other)
        if len_first > len_second:
            dif_of_len = len_first - len_second
            for index in range(len_second):
                list_of_sum.append(self[index] + other[index])
            for index in range(dif_of_len):
                list_of_sum.append(self[index + len_second])
        elif len_second > len_first:
            dif_of_len = len_second - len_first
            for index in range(len_first):
                list_of_sum.append(self[index] + other[index])
            for index in range(dif_of_len):
                list_of_sum.append(other[index + len_first])

        custom_list_of_sum = CustomList(list_of_sum)
        return custom_list_of_sum

    def __radd__(self, other):
        """Перегрузка оператора сложения"""
        list_of_sum = []
        len_first, len_second = len(self), len(other)
        if len_first > len_second:
            dif_of_len = len_first - len_second
            for index in range(len_second):
                list_of_sum.append(other[index] + self[index])
            for index in range(dif_of_len):
                list_of_sum.append(self[index + len_second])
        elif len_second > len_first:
            dif_of_len = len_second - len_first
            for index in range(len_first):
                list_of_sum.append(other[index] + self[index])
            for index in range(dif_of_len):
                list_of_sum.append(other[index + len_first])

        custom_list_of_sum = CustomList(list_of_sum)

        return custom_list_of_sum

    def __sub__(self, other):
        """Перегрузка оператора вычитание"""
        list_of_sub = []
        len_first, len_second = len(self), len(other)
        if len_first > len_second:
            dif_of_len = len_first - len_second
            for index in range(len_second):
                list_of_sub.append(self[index] - other[index])
            for index in range(dif_of_len):
                list_of_sub.append(self[index + len_second])
        elif len_second > len_first:
            dif_of_len = len_second - len_first
            for index in range(len_first):
                list_of_sub.append(self[index] - other[index])
            for index in range(dif_of_len):
                list_of_sub.append(- other[index + len_first])

        custom_list_of_sub = CustomList(list_of_sub)

        return custom_list_of_sub

    def __rsub__(self, other):
        """Перегрузка оператора вычитание"""
        list_of_sub = []
        len_first, len_second = len(self), len(other)
        if len_first > len_second:
            dif_of_len = len_first - len_second
            for index in range(len_second):
                list_of_sub.append(other[index] - self[index])
            for index in range(dif_of_len):
                list_of_sub.append(-self[index + len_second])
        elif len_second > len_first:
            dif_of_len = len_second - len_first
            for index in range(len_first):
                list_of_sub.append(other[index] - self[index])
            for index in range(dif_of_len):
                list_of_sub.append(other[index + len_first])

        custom_list_of_sub = CustomList(list_of_sub)

        return custom_list_of_sub

    def __str__(self):
        """Переопределение функции str"""
        return f"Кастомный список: {super().__str__()};" \
               f" Сумма его элементов: {sum(self)}"


if __name__ == "__main__":
    custom_list = CustomList(list(range(0)))
    print(custom_list)

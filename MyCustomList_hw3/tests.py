"""
Тесты к классу CustomList
"""
import unittest
from custom_list import CustomList


def is_eq_lists(list1, list2):
    """Функция проводящая поэлементное сравнение"""
    len1, len2 = len(list1), len(list2)
    if len1 != len2:
        return False
    for i in range(len1):
        if list1[i] != list2[i]:
            return False
    return True


class MyTestCase(unittest.TestCase):
    """ Класс для юнит тестов"""
    def test_init(self):
        """Тест на правильную работу конструктора"""
        custom_list1 = CustomList()
        custom_list2 = CustomList(list(range(5)))
        self.assertTrue(is_eq_lists(custom_list1, []), True)
        self.assertTrue(is_eq_lists(custom_list2, list(range(5))), True)

    def test_lt(self):
        """Тест на правильную работу перегрузки оператора ==
        CustomList == CustomList
        CustomList == standard list"""
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(5)))
        self.assertFalse(custom_list1 < custom_list2, False)
        custom_list1 = CustomList(list(range(3)))
        custom_list2 = CustomList(list(range(5)))
        self.assertTrue(custom_list1 < custom_list2, True)
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(3)))
        self.assertFalse(custom_list1 < custom_list2, False)

        custom_list1 = CustomList(list(range(5)))
        standard_list = list(range(5))
        self.assertFalse(custom_list1 < standard_list, False)
        custom_list1 = CustomList(list(range(3)))
        standard_list = list(range(5))
        self.assertTrue(custom_list1 < standard_list, True)
        standard_list = list(range(5))
        custom_list2 = CustomList(list(range(3)))
        self.assertFalse(standard_list < custom_list2, False)

    def test_le(self):
        """Тест на правильную работу перегрузки оператора ==
        CustomList == CustomList
        CustomList == standard list"""
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(5)))
        self.assertTrue(custom_list1 <= custom_list2, True)
        custom_list1 = CustomList(list(range(3)))
        custom_list2 = CustomList(list(range(5)))
        self.assertTrue(custom_list1 <= custom_list2, True)
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(3)))
        self.assertFalse(custom_list1 <= custom_list2, False)

        custom_list1 = CustomList(list(range(5)))
        standard_list = list(range(5))
        self.assertTrue(custom_list1 <= standard_list, True)
        custom_list1 = CustomList(list(range(3)))
        standard_list = list(range(5))
        self.assertTrue(custom_list1 <= standard_list, True)
        standard_list = list(range(5))
        custom_list2 = CustomList(list(range(3)))
        self.assertFalse(standard_list <= custom_list2, False)

    def test_eq(self):
        """Тест на правильную работу перегрузки оператора ==
        CustomList == CustomList
        CustomList == standard list"""
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(5)))
        self.assertTrue(custom_list1 == custom_list2, True)
        custom_list1 = CustomList(list(range(3)))
        custom_list2 = CustomList(list(range(5)))
        self.assertFalse(custom_list1 == custom_list2, False)
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(3)))
        self.assertFalse(custom_list1 == custom_list2, False)

        custom_list1 = CustomList(list(range(5)))
        standard_list = list(range(5))
        self.assertTrue(custom_list1 == standard_list, True)
        custom_list1 = CustomList(list(range(3)))
        standard_list = list(range(5))
        self.assertFalse(custom_list1 == standard_list, False)
        standard_list = list(range(5))
        custom_list2 = CustomList(list(range(3)))
        self.assertFalse(standard_list == custom_list2, False)

    def test_ne(self):
        """Тест на правильную работу перегрузки оператора ==
        CustomList == CustomList
        CustomList == standard list"""
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(5)))
        self.assertFalse(custom_list1 != custom_list2, False)
        custom_list1 = CustomList(list(range(3)))
        custom_list2 = CustomList(list(range(5)))
        self.assertTrue(custom_list1 != custom_list2, True)
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(3)))
        self.assertTrue(custom_list1 != custom_list2, True)

        custom_list1 = CustomList(list(range(5)))
        standard_list = list(range(5))
        self.assertFalse(custom_list1 != standard_list, False)
        custom_list1 = CustomList(list(range(3)))
        standard_list = list(range(5))
        self.assertTrue(custom_list1 != standard_list, True)
        standard_list = list(range(5))
        custom_list2 = CustomList(list(range(3)))
        self.assertTrue(standard_list != custom_list2, True)

    def test_gt(self):
        """Тест на правильную работу перегрузки оператора ==
        CustomList == CustomList
        CustomList == standard list"""
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(5)))
        self.assertFalse(custom_list1 > custom_list2, False)
        custom_list1 = CustomList(list(range(3)))
        custom_list2 = CustomList(list(range(5)))
        self.assertFalse(custom_list1 > custom_list2, False)
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(3)))
        self.assertTrue(custom_list1 > custom_list2, True)

        custom_list1 = CustomList(list(range(5)))
        standard_list = list(range(5))
        self.assertFalse(custom_list1 > standard_list, False)
        custom_list1 = CustomList(list(range(3)))
        standard_list = list(range(5))
        self.assertFalse(custom_list1 > standard_list, False)
        standard_list = list(range(5))
        custom_list2 = CustomList(list(range(3)))
        self.assertTrue(standard_list > custom_list2, True)

    def test_ge(self):
        """Тест на правильную работу перегрузки оператора ==
        CustomList == CustomList
        CustomList == standard list"""
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(5)))
        self.assertTrue(custom_list1 >= custom_list2, True)
        custom_list1 = CustomList(list(range(3)))
        custom_list2 = CustomList(list(range(5)))
        self.assertFalse(custom_list1 >= custom_list2, False)
        custom_list1 = CustomList(list(range(5)))
        custom_list2 = CustomList(list(range(3)))
        self.assertTrue(custom_list1 >= custom_list2, True)

        custom_list1 = CustomList(list(range(5)))
        standard_list = list(range(5))
        self.assertTrue(custom_list1 >= standard_list, True)
        custom_list1 = CustomList(list(range(3)))
        standard_list = list(range(5))
        self.assertFalse(custom_list1 >= standard_list, False)
        standard_list = list(range(5))
        custom_list2 = CustomList(list(range(3)))
        self.assertTrue(standard_list >= custom_list2, True)

    def test_add(self):
        """Тест перегрузки оператора +
        CustomList() + CustomList()
        CustomList() + CustomList()
        CustomList() + standard list
        standard list + CustomList()"""
        custom_list1 = CustomList([5, 1, 3, 7])
        custom_list2 = CustomList([1, 2, 7])
        result = custom_list1 + custom_list2
        self.assertTrue(is_eq_lists(custom_list1, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(custom_list2, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(result, [6, 3, 10, 7]), True)
        self.assertEqual(type(result), CustomList)

        custom_list1 = CustomList([1, 2, 7])
        custom_list2 = CustomList([5, 1, 3, 7])
        result = custom_list1 + custom_list2
        self.assertTrue(is_eq_lists(custom_list1, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(custom_list2, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(result, [6, 3, 10, 7]), True)
        self.assertEqual(type(result), CustomList)

        custom_list1 = CustomList([5, 1, 3, 7])
        standard_list = [1, 2, 7]
        result = custom_list1 + standard_list
        self.assertTrue(is_eq_lists(custom_list1, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(standard_list, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(result, [6, 3, 10, 7]), True)
        self.assertEqual(type(result), CustomList)

        standard_list = [1, 2, 7]
        custom_list2 = CustomList([5, 1, 3, 7])
        result = standard_list + custom_list2
        self.assertTrue(is_eq_lists(standard_list, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(custom_list2, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(result, [6, 3, 10, 7]), True)
        self.assertEqual(type(result), CustomList)

        custom_list1 = CustomList([1, 2, 7])
        standard_list = [5, 1, 3, 7]
        result = custom_list1 + standard_list
        self.assertTrue(is_eq_lists(custom_list1, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(standard_list, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(result, [6, 3, 10, 7]), True)
        self.assertEqual(type(result), CustomList)

        standard_list = [5, 1, 3, 7]
        custom_list2 = CustomList([1, 2, 7])
        result = standard_list + custom_list2
        self.assertTrue(is_eq_lists(standard_list, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(custom_list2, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(result, [6, 3, 10, 7]), True)
        self.assertEqual(type(result), CustomList)

    def test_sub(self):
        """Тест перегрузки оператора -
        CustomList() - CustomList()
        CustomList() - CustomList()
        CustomList() - standard list
        standard list - CustomList()"""
        custom_list1 = CustomList([5, 1, 3, 7])
        custom_list2 = CustomList([1, 2, 7])
        result = custom_list1 - custom_list2
        self.assertTrue(is_eq_lists(custom_list1, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(custom_list2, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(result, [4, -1, -4, 7]), True)
        self.assertEqual(type(result), CustomList)

        custom_list1 = CustomList([1, 2, 7])
        custom_list2 = CustomList([5, 1, 3, 7])
        result = custom_list1 - custom_list2
        self.assertTrue(is_eq_lists(custom_list1, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(custom_list2, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(result, [-4, 1, 4, -7]), True)
        self.assertEqual(type(result), CustomList)

        custom_list1 = CustomList([5, 1, 3, 7])
        standard_list = [1, 2, 7]
        result = custom_list1 - standard_list
        self.assertTrue(is_eq_lists(custom_list1, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(standard_list, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(result, [4, -1, -4, 7]), True)
        self.assertEqual(type(result), CustomList)

        standard_list = [1, 2, 7]
        custom_list2 = CustomList([5, 1, 3, 7])
        result = standard_list - custom_list2
        self.assertTrue(is_eq_lists(standard_list, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(custom_list2, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(result, [-4, 1, 4, -7]), True)
        self.assertEqual(type(result), CustomList)

        custom_list1 = CustomList([1, 2, 7])
        standard_list = [5, 1, 3, 7]
        result = custom_list1 - standard_list
        self.assertTrue(is_eq_lists(custom_list1, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(standard_list, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(result, [-4, 1, 4, -7]), True)
        self.assertEqual(type(result), CustomList)

        standard_list = [5, 1, 3, 7]
        custom_list2 = CustomList([1, 2, 7])
        result = standard_list - custom_list2
        self.assertTrue(is_eq_lists(standard_list, [5, 1, 3, 7]), True)
        self.assertTrue(is_eq_lists(custom_list2, [1, 2, 7]), True)
        self.assertTrue(is_eq_lists(result, [4, -1, -4, 7]), True)
        self.assertEqual(type(result), CustomList)

    def test_str(self):
        """Тест переопределения функции str()"""
        custom_list = CustomList(list(range(5)))
        self.assertEqual(str(custom_list), f"Кастомный список:"
                                           f" {list(range(5))};"
                                           f" Сумма его элементов: {10}")
        custom_list = CustomList()
        self.assertEqual(str(custom_list), f"Кастомный список:"
                                           f" {[]};"
                                           f" Сумма его элементов: {0}")


if __name__ == '__main__':
    unittest.main()

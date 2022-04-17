"""
Тесты к классу CustomList
"""
import unittest
from descriptor import Data
from meta_class import CustomClass


class MyTestCase(unittest.TestCase):
    """ Класс для юнит тестов"""
    def test_custom_class_init(self):
        """Тест на проверку работы инициализации"""
        custom = CustomClass()
        self.assertEqual(custom.custom_x, 50)
        self.assertEqual(CustomClass.custom_x, 50)
        self.assertEqual(custom.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.assertEqual(custom.x, 50)
        with self.assertRaises(AttributeError):
            self.assertEqual(CustomClass.x, 50)
        with self.assertRaises(AttributeError):
            self.assertEqual(custom.val, 99)

        custom = CustomClass(1)
        self.assertEqual(custom.custom_x, 50)
        self.assertEqual(CustomClass.custom_x, 50)
        self.assertEqual(custom.custom_val, 1)
        with self.assertRaises(AttributeError):
            self.assertEqual(custom.x, 50)
        with self.assertRaises(AttributeError):
            self.assertEqual(CustomClass.x, 50)
        with self.assertRaises(AttributeError):
            self.assertEqual(custom.val, 1)

    def test_custom_class_line(self):
        """Тест на проверку работы метода"""
        custom = CustomClass()
        self.assertEqual(custom.custom_line(), 50)
        with self.assertRaises(AttributeError):
            custom.line()  # ошибка

    def test_custom_class_str(self):
        """Тест на проверку работы метода"""
        custom = CustomClass()
        self.assertEqual(str(custom), "Custom_by_metaclass")

    def test_descriptors(self):
        """Тест на правильную работу дескриптора"""
        data = Data()
        self.assertEqual(data.rating, 0)
        self.assertEqual(data.name, "None")
        self.assertEqual(data.price, 1)
        data.rating = -12
        data.name = "KING"
        data.price = 1500
        self.assertEqual(data.rating, -12)
        self.assertEqual(data.name, "KING")
        self.assertEqual(data.price, 1500)

        data.rating = 12
        data.name = "123king123"
        data.price = 15
        self.assertEqual(data.rating, 12)
        self.assertEqual(data.name, "123king123")
        self.assertEqual(data.price, 15)

        with self.assertRaises(Exception):
            data.rating = 1.5
        with self.assertRaises(Exception):
            data.rating = 0.5
        with self.assertRaises(Exception):
            data.rating = -1.5
        with self.assertRaises(Exception):
            data.name = 10
        with self.assertRaises(Exception):
            data.name = 0
        with self.assertRaises(Exception):
            data.name = -10
        with self.assertRaises(Exception):
            data.price = 1.5
        with self.assertRaises(Exception):
            data.price = 0.5
        with self.assertRaises(Exception):
            data.price = -1.5
        with self.assertRaises(Exception):
            data.price = 0
        with self.assertRaises(Exception):
            data.price = -1
        with self.assertRaises(Exception):
            data.price = -10

    def test_delete_data(self):
        """Тест на правильную работу функции Data.delete_data()"""
        data = Data()
        data.rating = -12
        data.name = "KING"
        data.price = 1500
        data.delete_data()
        self.assertEqual(data.rating, 0)
        self.assertEqual(data.name, "None")
        self.assertEqual(data.price, 1)

    def test_str(self):
        """Тест на правильную работу функции Data.print_data()"""
        data = Data()
        data.rating = -12
        data.name = "KING"
        data.price = 1500
        self.assertEqual(str(data), "rating = -12\n"
                                    "name = KING\n"
                                    "price = 1500\n")


if __name__ == '__main__':
    unittest.main()

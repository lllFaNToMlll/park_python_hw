"""
Тесты
"""
import unittest
from random import randint
import time
from multiplication_of_matrix_rows import mul_of_mat_rows_py
import cutils


class MyTestCase(unittest.TestCase):
    """Класс для тестов"""
    def test_mul_of_mat_rows_py(self):
        """Тест правильности работы Python кода"""
        matrix = [
            [1, 2, 3],
            [5, 6, 7],
            [8, 9, 10],
            [11, 12, 13],
            [15, 16, 17]
        ]
        result = mul_of_mat_rows_py(matrix)
        self.assertEqual([6600, 20736, 46410], result)

    def test_mul_of_mat_rows_cy(self):
        """Тест правильности работы Cython кода"""
        matrix = [
            [1, 2, 3],
            [5, 6, 7],
            [8, 9, 10],
            [11, 12, 13],
            [15, 16, 17]
        ]
        result = cutils.mul_of_mat_rows(matrix)
        self.assertEqual([6600, 20736, 46410], result)

    def test_py_cy_result_and_profit(self):
        """Тест для сравнения времени работы
            Cython и Python кода, а также их
            результатов"""
        row_len = 3000
        col_len = 3000
        matrix = [
            [randint(1, 9) for _ in range(row_len)] for _ in range(col_len)
        ]

        start = time.time()
        result_py = mul_of_mat_rows_py(matrix)
        end = time.time()
        py_time = end - start

        start = time.time()
        result_cy = cutils.mul_of_mat_rows(matrix)
        end = time.time()
        c_time = end - start

        self.assertEqual(result_py, result_cy)
        self.assertGreater(py_time, c_time, "Cython почему-то медленнее :(")


if __name__ == '__main__':
    unittest.main()

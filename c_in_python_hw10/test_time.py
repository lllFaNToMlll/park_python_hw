"""
Файл для сравнения времени работы cython и python кода
"""
from random import randint
import time
from multiplication_of_matrix_rows import mul_of_mat_rows_py, print_matrix
import cutils


if __name__ == "__main__":
    row_len = input("Введите количество строк в матрице: ")
    while True:
        if not row_len.isnumeric():
            row_len = input("Введите целое число для "
                            "количества строк в матрице: ")
            continue
        if int(row_len) < 1:
            row_len = input("Введите целое число (>=1) для "
                            "количества строк в матрице: ")
            continue

        row_len = int(row_len)
        break

    col_len = input("Введите количество столбцов в матрице: ")
    while True:
        if not col_len.isnumeric():
            col_len = input("Введите целое число для "
                            "количества столбцов в матрице: ")
            continue
        if int(col_len) < 1:
            col_len = input("Введите целое число (>=1) для"
                            " количества столбцов в матрице: ")
            continue

        col_len = int(col_len)
        break

    matrix = [[randint(1, 9) for _ in range(col_len)] for _ in range(row_len)]
    if row_len < 20 and col_len < 20:
        print_matrix(matrix)

    start = time.time()
    result = mul_of_mat_rows_py(matrix)
    end = time.time()
    py_time = end - start
    if row_len < 20 and col_len < 20:
        print(result)
    print(f"Python time = {py_time}")

    start = time.time()
    result = cutils.mul_of_mat_rows(matrix)
    end = time.time()
    c_time = end - start
    if row_len < 20 and col_len < 20:
        print(result)
    print(f"Cython time = {c_time}")

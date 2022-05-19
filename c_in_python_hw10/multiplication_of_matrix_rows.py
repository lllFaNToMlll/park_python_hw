"""
Поэлементное умножение строк матрицы
"""


def mul_of_mat_rows_py(matrix):
    """Функция поэлементного умножение строк матрицы"""
    row_len = len(matrix)
    col_len = len(matrix[0])
    result = [1 for i in range(col_len)]

    for col_idx in range(col_len):
        for row_idx in range(row_len):
            result[col_idx] *= matrix[row_idx][col_idx]

    return result


def print_matrix(matrix):
    """Функция печати матрицы в красивом виде"""
    row_len = len(matrix)
    col_len = len(matrix[0])
    for row_idx in range(row_len):
        for col_idx in range(col_len):
            print(matrix[row_idx][col_idx], end="  ")

        print(" ")

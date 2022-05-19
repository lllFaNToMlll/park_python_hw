cpdef mul_of_mat_rows(list matrix):
    cdef row_len = len(matrix)
    cdef col_len = len(matrix[0])
    cdef result = [1 for i in range(col_len)]

    for col_idx in range(col_len):
        for row_idx in range(row_len):
            result[col_idx] *= matrix[row_idx][col_idx]

    return result

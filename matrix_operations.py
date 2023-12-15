import math
from ascii_operations import *

def matrix_product(matrix_a, matrix_b):
    result_matrix = [[0 for i in range(len(matrix_b[0]))] for i in range(len(matrix_a))]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_a[0])):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result_matrix

def key_to_matrix(ascii_arr):
    matrix_size = math.ceil(math.sqrt(len(ascii_arr)))
    num_matrix = []
    ascii_arr_index = 0

    for i in range(matrix_size):
        num_matrix.append([])
        for n in range(matrix_size):
            if (ascii_arr_index < len(ascii_arr)):
                num_matrix[i].append(ascii_arr[ascii_arr_index])
                ascii_arr_index += 1
            else:
                num_matrix[i].append(0)
    return num_matrix

def content_to_matrix(ascii_arr, nb_cols):
    num_matrix = []
    matrix_nb_rows = math.ceil(len(ascii_arr) / nb_cols)
    ascii_arr_index = 0

    for i in range(matrix_nb_rows):
        num_matrix.append([])
        for n in range(nb_cols):
            if (ascii_arr_index < len(ascii_arr)):
                num_matrix[i].append(ascii_arr[ascii_arr_index])
                ascii_arr_index += 1
            else:
                num_matrix[i].append(0)
    return num_matrix

def get_key_matrix(key):
    key_arr = string_to_ascii_arr(key)
    return key_to_matrix(key_arr)

def get_content_matrix(content, key):
    content_arr = string_to_ascii_arr(content)
    return content_to_matrix(content_arr, len(key[0]))

def transpose_matrix(matrix):
    new_matrix = []
    index = 0
    for i in range(len(matrix[0])):
        new_matrix.append([])
        for row in matrix:
            new_matrix[index].append(row[i])
        index += 1
    return new_matrix

def get_determinant(matrix):
    determinant = 0
    if (len(matrix) == 2):
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    if (len(matrix) == 1):
        return matrix[0][0]
    
    sign = 1
    for i in range(len(matrix[0])):
        new_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
        determinant += matrix[0][i] * get_determinant(new_matrix) * sign
        sign = -sign
    return determinant

def get_cofactor(matrix, i, j):
    new_matrix = [[matrix[e][n] for n in range(len(matrix[0])) if n != j] for e in range(len(matrix)) if e != i]    
    return (-1)**(i+j) * get_determinant(new_matrix)

def get_cofactor_matrix(matrix):
    cofactor_matrix = []
    for i in range(len(matrix)):
        cofactor_matrix.append([])
        for j in range(len(matrix[i])):
            cofactor_matrix[i].append(get_cofactor(matrix, i, j))
    return cofactor_matrix

def inverse_key(cofactor_matrix, key_matrix):
    transposed = transpose_matrix(cofactor_matrix)
    determinant_rev = 1 / get_determinant(key_matrix)
    for i in range(len(transposed)):
        for j in range(len(transposed[i])):
            transposed[i][j] = transposed[i][j] * determinant_rev
    return transposed
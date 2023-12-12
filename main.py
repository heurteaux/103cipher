#!/usr/bin/python3
import math

def matrix_product(matrix_a, matrix_b):
    result_matrix = [[0 for i in range(len(matrix_b[0]))] for i in range(len(matrix_a))]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_a[0])):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result_matrix

def string_to_ascii_arr(input_string):
    ascii_arr = []
    for character in input_string:
        ascii_arr.append(ord(character))
    return ascii_arr

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

def encrypt_message(message, key):
    key_matrix = get_key_matrix(key)
    content_matrix = get_content_matrix(message, key_matrix)
    return matrix_product(content_matrix, key_matrix)

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

def transpose_matrix(matrix):
    new_matrix = []
    index = 0
    for i in range(len(matrix[0])):
        new_matrix.append([])
        for row in matrix:
            new_matrix[index].append(row[i])
        index += 1
    return new_matrix

def inverse_key(matrix):
    matrix = transpose_matrix(matrix)
    determinant = get_determinant(matrix)
    determinant_rev = 1 / determinant
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] * determinant_rev
    return matrix

def print_matrix(matrix):
    for element in matrix:
        print(element)

key = "Homer S"
content = "Just because I don't care doesn't mean I don't understand."

for element in encrypt_message(content, key):
    for scn_element in element:
        print(scn_element, end=" ")
print("")
ascii_key = string_to_ascii_arr(key)
key_matrix = key_to_matrix(ascii_key)

print_matrix(key_matrix)
print_matrix(inverse_key(key_matrix))
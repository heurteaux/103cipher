from matrix_operations import *
from displaying import *
import math

def format_encrypted_content(encrypted_content, key_size):
    elements_array = encrypted_content.split()
    num_matrix = []

    for i in range(len(elements_array)):
        elements_array[i] = int(elements_array[i])
    matrix_nb_rows = math.ceil(len(elements_array) / key_size)
    ascii_arr_index = 0

    for i in range(matrix_nb_rows):
        num_matrix.append([])
        for n in range(key_size):
            if (ascii_arr_index < len(elements_array)):
                num_matrix[i].append(elements_array[ascii_arr_index])
                ascii_arr_index += 1
    return num_matrix


def decrypt_content(encrypted_content, key):
    if len(key) == 1:
        key_value = ord(key)
        if key_value == 0:
            print("Decryption error: Key cannot be zero")
            return
        inverse_key_value = pow(key_value, -1, 256)
        print("Key matrix:\n", inverse_key_value, "\n", sep="")
        print("Decrypted message:")
        for num in map(int, encrypted_content.split()):
            decrypted_char = (num * inverse_key_value) % 256
            print(chr(decrypted_char), end="")
        print("")
    else:
        key_matrix = get_key_matrix(key)
        display_key_matrix(key_matrix)
        print("")
        content_matrix = format_encrypted_content(encrypted_content, len(key_matrix))
        decode_key = inverse_key(get_cofactor_matrix(key_matrix), key_matrix)

        display_decrypted_content(matrix_product(content_matrix, decode_key))
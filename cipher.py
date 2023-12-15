from matrix_operations import *
from displaying import *

def encrypt_message(message, key):
    if len(key) == 1:
        key_value = ord(key)
        print("Encrypted message:")
        for char in message:
            encrypted_char = (ord(char) * key_value) % 256
            print(encrypted_char, end=" ")
        print("")
    else:
        key_matrix = get_key_matrix(key)
        display_key_matrix(key_matrix)
        content_matrix = get_content_matrix(message, key_matrix)
        display_encrypted_message(matrix_product(content_matrix, key_matrix))

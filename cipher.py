from displaying import *
from matrix_operations import *

def encrypt_message(message, key):
    key_matrix = get_key_matrix(key)
    display_key_matrix(key_matrix)
    content_matrix = get_content_matrix(message, key_matrix)
    display_encrypted_message(matrix_product(content_matrix, key_matrix))
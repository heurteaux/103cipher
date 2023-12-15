def display_decrypted_content(decrypted_content):
    print("Decrypted message:")
    for row in decrypted_content:
        for element in row:
            if round(element) != 0:
                print(chr(round(element)), end="")
    print("")

def display_encrypted_message(message):
    print("\nEncrypted message:")
    for i in range(len(message)):
        for j in range(len(message[i])):
            if (i == len(message) - 1 and j == len(message[i]) - 1):
                print(message[i][j])
            else:
                print(message[i][j], end=" ")

def display_key_matrix(key):
    print("Key matrix:")
    for i in range(len(key)):
        for j in range(len(key[i])):
            if not (j == len(key[i]) - 1):
                print(key[i][j], end="\t")
            else:
                print(key[i][j], end="")
        print("")

def print_matrix(matrix):
    for element in matrix:
        print(element)

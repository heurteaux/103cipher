def string_to_ascii_arr(input_string):
    ascii_arr = []
    for character in input_string:
        ascii_arr.append(ord(character))
    return ascii_arr
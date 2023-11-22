plain_text = "helloworld"
keyword = "bhavya"

def generate_playfair_matrix(key):
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I")
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    remaining_chars = [char for char in alphabet if char not in key_set]

    playfair_matrix = []
    for char in key:
        if char not in playfair_matrix:
            playfair_matrix.append(char)
    for char in remaining_chars:
        playfair_matrix.append(char)

    matrix = [['' for i in range(5)] for j in range(5)]

    i = 0
    for j in range(0, len(playfair_matrix), 5):
        matrix[i] = playfair_matrix[j:j + 5]
        i += 1

    return matrix


def prepare_input(text):
    text = text.replace(" ", "").upper()
    text = text.replace("J", "I")
    prepared_text = ""
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            prepared_text += text[i] + "X"
            i += 1
        elif text[i] == text[i + 1]:
            prepared_text += text[i] + "X"
            i += 1
        else:
            prepared_text += text[i] + text[i + 1]
            i += 2
    return prepared_text


def find_coordinates(matrix, char):
    row = 0
    col = 0

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    text = prepare_input(plaintext)
    ciphertext = ""

    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i + 1]

        row1, col1 = find_coordinates(matrix, text[i])
        row2, col2 = find_coordinates(matrix, text[i + 1])

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext


def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    text = prepare_input(ciphertext)
    plain_text = ""

    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i + 1]

        row1, col1 = find_coordinates(matrix, text[i])
        row2, col2 = find_coordinates(matrix, text[i + 1])

        if row1 == row2:
            plain_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plain_text += matrix[row1][col2] + matrix[row2][col1]

    return plain_text


print("Cipher Text:", playfair_encrypt(plain_text, keyword))
print("Plain Text:", playfair_decrypt(playfair_encrypt(plain_text, keyword), keyword))

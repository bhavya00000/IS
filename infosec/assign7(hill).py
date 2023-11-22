def prepare_plaintext(plaintext):
    plaintext = plaintext.replace(" ", "").upper()
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    return plaintext

def text_to_matrix(text):
    return [ord(char) - ord('A') for char in text]

def matrix_to_text(matrix):
    return ''.join([chr(int(val) + ord('A')) for val in matrix])

def key_to_matrix(key):
    key = key.upper()
    key_matrix = [[ord(key[0]) - ord('A'), ord(key[1]) - ord('A')],[ord(key[2]) - ord('A'), ord(key[3]) - ord('A')]]
    return key_matrix

def encrypt(plaintext, key_matrix):
    plaintext = prepare_plaintext(plaintext)
    plaintext_matrix = text_to_matrix(plaintext)
    ciphertext_matrix = []
    for i in range(0, len(plaintext_matrix), 2):
        block = plaintext_matrix[i:i + 2]
        encrypted_block = [(key_matrix[0][0] * block[0] + key_matrix[0][1] * block[1]) % 26, (key_matrix[1][0] * block[0] + key_matrix[1][1] * block[1]) % 26]
        ciphertext_matrix.extend(encrypted_block)
    ciphertext = matrix_to_text(ciphertext_matrix)
    return ciphertext


def mod_inverse(a, m):
    for i in range(26):
        if (a * i) % m == 1:
            return i
    return None

def decrypt(ciphertext, key_matrix):
    determinant = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26
    modular_inverse = mod_inverse(determinant, 26)
    if modular_inverse is None:
        return "The key is not invertible. Cannot decrypt."
    key_matrix_inverse = [[(key_matrix[1][1] * modular_inverse) % 26, (-key_matrix[0][1] * modular_inverse) % 26], [(-key_matrix[1][0] * modular_inverse) % 26, (key_matrix[0][0] * modular_inverse) % 26]]
    ciphertext_matrix = text_to_matrix(ciphertext)
    decrypted_matrix = []
    for i in range(0, len(ciphertext_matrix), 2):
        block = ciphertext_matrix[i:i + 2]
        decrypted_block = [(key_matrix_inverse[0][0] * block[0] + key_matrix_inverse[0][1] * block[1]) % 26, (key_matrix_inverse[1][0] * block[0] + key_matrix_inverse[1][1] * block[1]) % 26 ]
        decrypted_matrix.extend(decrypted_block)
    decrypted_text = matrix_to_text(decrypted_matrix)
    return decrypted_text
key_word = input("Enter the keyword: ")
plaintext = input("Enter the plaintext: ")
key_matrix = key_to_matrix(key_word)
ciphertext = encrypt(plaintext, key_matrix)
print("Ciphertext:", ciphertext)
decrypted_text = decrypt(ciphertext, key_matrix)
print("Decrypted Text:", decrypted_text)

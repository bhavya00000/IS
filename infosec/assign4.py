def rail_fence_encrypt(text, key):
    encrypted = [''] * key
    index = 0
    direction = 1

    for char in text:
        encrypted[index] += char
        if index == 0:
            direction = 1
        elif index == key - 1:
            direction = -1
        index += direction

    return ''.join(encrypted)


def rail_fence_decrypt(text, key):
    decrypted = [''] * key
    index = 0
    direction = 1

    for char in text:
        decrypted[index] += '*'
        if index == 0:
            direction = 1
        elif index == key - 1:
            direction = -1
        index += direction

    text_index = 0
    for i in range(key):
        for j in range(len(decrypted[i])):
            decrypted[i] = decrypted[i][:j] + text[text_index] + decrypted[i][j + 1:]
            text_index += 1

    result = ''
    index = 0
    direction = 1

    for i in range(len(text)):
        result += decrypted[index][0]
        decrypted[index] = decrypted[index][1:]
        if index == 0:
            direction = 1
        elif index == key - 1:
            direction = -1
        index += direction

    return result

    # Example usage


text = "railfencecipherexample"
key = 3
encrypted_text = rail_fence_encrypt(text, key)
print("Encrypted:", encrypted_text)

decrypted_text = rail_fence_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(message, key):
    message = message.lower()
    key = key.lower()
    key_length = len(key)

    encrypted_text = [""] * key_length

    while (True):
        if len(message) % len(key) != 0:
            message = message + 'z'
        elif len(message) % len(key) == 0:
            break
        else:
            pass

    for column in range(key_length):
        pointer = column
        while pointer < len(message):
            encrypted_text[column] += message[pointer]
            pointer += key_length


    key_string = [*key]


    key_index = []
    for i in key_string:
        if i in alphabets:
            key_index.append(alphabets.index(i))
    print(key_index)


    sorted_key_index = sorted(key_index)
    encrypt = []
    for i in sorted_key_index:
        index = key_index.index(i)
        encrypt.append(encrypted_text[index])

    encrypted_final = ''.join(encrypt)
    print(encrypted_final)


def decryption(encrypted, key):
    encrypted = encrypted.lower()
    key = key.lower()

    plain_text = []

    key_length = len(key)
    encrypted_message_length = len(encrypted)

    divide = int(encrypted_message_length / key_length)

    encrypted_text_list = []
    for i in range(len(key)):
        s = encrypted[divide * i:divide * (i + 1)]
        encrypted_text_list.append(s)

    key_string = [*key]

    key_index = []
    for i in key_string:
        if i in alphabets:
            key_index.append(alphabets.index(i))

    sorted_key_index = sorted(key_index)


    encrypted_column_vise = []
    for i in key_index:
        index = sorted_key_index.index(i)
        encrypted_column_vise.append(encrypted_text_list[index])


    for i in range(divide):
        for j in range(len(key)):
            plain_text.append(encrypted_column_vise[j][i])

    plain = ''.join(plain_text)
    print(plain)


def main():
    print("Enter the message to be encrypted")
    message = input()
    print("Enter the key")
    key = input()
    encryption(message, key)
    print("Enter the message to be decrypted")
    encrypted = input()
    print("Enter the key")
    key = input()
    decryption(encrypted, key)


if __name__ == "__main__":
    main()

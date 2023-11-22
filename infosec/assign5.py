def encrypt(plaintext, key):
    plaintext = plaintext.lower().replace(" ", "")
    key = key.lower()
    cipherkey = [0] * len(plaintext)
    order = 0
    for i in range(len(plaintext)):
        cipherkey[i] = key[order]
        order += 1
        if order == len(key):
            order = 0

    encrypt_text = ""
    for i in range(len(plaintext)):
        character = plaintext[i]
        key = cipherkey[i]
        encrypt_text += chr((ord(character) + ((ord(key) - 97) % 26) - 97) % 26 + 97)

    return encrypt_text


def decrypt(cipher, key):
    cipher = cipher.lower().replace(" ", "")
    key = key.lower()
    cipherkey = [0] * len(cipher)
    order = 0
    for i in range(len(cipher)):
        cipherkey[i] = key[order]
        order += 1
        if order == len(key):
            order = 0

    decrypt_text = ""
    for i in range(len(cipher)):
        character = cipher[i]
        key = cipherkey[i]
        decrypt_text += chr((ord(character) - ((ord(key) - 97) % 26) - 97) % 26 + 97)

    return decrypt_text


def main():
    while True:
        print("1.Encrypt")
        print("2.Decrypt")
        print("3.Exit")
        choice = int(input("Enter the choice number : "))
        if choice == 1:
            text = input("Enter the Plain Text : ")
            key = input("enter the key : ")
            print("Encrypted Text : ", encrypt(text, key))
        elif choice == 2:
            text = input("Enter the Cipher Text : ")
            key = input("enter the key : ")
            print("Decrypted Text : ", decrypt(text, key))
        elif choice == 3:
            print("Exit")
            break
        else:
            print("Invalid choice")


main()

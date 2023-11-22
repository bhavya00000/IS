def encrypt(text, shift):
    result = ""
    text = text.lower()
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


def decrypt(text, shift):
    result = ""
    text = text.lower()
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) - shift - 97) % 26 + 97)
    return result


def brute_force(text):
    for i in range(26):
        print("Shift ",i, ":  ", decrypt(text, i))


def frequency_analysis(text):
    freq = {}
    for i in range(len(text)):
        char = text[i]
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    print(freq)


def main():
    print("Enter the text to be encrypted")
    text = input()
    print("Enter the shift value")
    shift = int(input())
    print("The encrypted text is")
    print(encrypt(text, shift))
    print("The decrypted text is")
    print(decrypt(encrypt(text, shift), shift))
    print("The brute force decryption is")
    brute_force(encrypt(text, shift))
    print("The frequency analysis is")
    frequency_analysis(encrypt(text, shift))


main()
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def RSA(p, q, message):
    n = p * q
    t = (p - 1) * (q - 1)

    # Find e (public key exponent)
    e = 2
    while e < t:
        if calculate_gcd(e, t) == 1:
            break
        e += 1

    # Find d (private key exponent)
    j = 2
    while True:
        if (j * e) % t == 1:
            d = j
            break
        j += 1

    ct = (message ** e) % n
    print(f"Encrypted message is {ct}")

    mes = (ct ** d) % n
    print(f"Decrypted message is {mes}")

p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
message = int(input("Enter the message to be encrypted: "))

RSA(p, q, message)

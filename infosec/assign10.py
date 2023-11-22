import random

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randrange(1, phi)
        if calculate_gcd(e, phi) == 1: # coprime or not
            break
    d = mod_inverse(e, phi)
    return ((n, e), (n, d))

def sign_message(private_key, message):
    n, d = private_key
    signature = pow(message, d, n)
    return signature

def verify_signature(public_key, message, signature):
    n, e = public_key
    decrypted_signature = pow(signature, e, n)
    return message == decrypted_signature

p = generate_prime(10)
q = generate_prime(10)
public_key, private_key = generate_keypair(p, q)
print(f'Public key: {public_key} \nPrivate key: {private_key}')

message = 10
print("Original message:", message)

signature = sign_message(private_key, message)
print("Signature:", signature)

if verify_signature(public_key, message, signature):
    print("Signature is valid.")
else:
    print("Signature is invalid.")

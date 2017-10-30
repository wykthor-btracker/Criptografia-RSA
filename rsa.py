import random
import fractions
from prime_gen import generate_random_prime

def extended_gcd(a, b):
    """Returns pair (x, y) such that xa + yb = gcd(a, b)"""
    x, lastx, y, lasty = 0, 1, 1, 0
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return lastx, lasty


def multiplicative_inverse(e, n):
    """Find the multiplicative inverse of e mod n."""
    x, y = extended_gcd(e, n)
    if x < 0:
        return n + x
    return x


def rsa_generate_key(bits):
    p = generate_random_prime(int(bits / 2))
    q = generate_random_prime(int(bits / 2))
    # Ensure q != p, though for large values of bits this is
    # statistically very unlikely
    while q == p:
        q = generate_random_prime(int(bits / 2))
    n = p * q
    phi = (p - 1) * (q - 1)
    # Here we pick a random e, but a fixed value for e can also be used.
    while True:
        e = random.randint(3, phi - 1)
        if fractions.gcd(e, phi) == 1:
            break
    d = multiplicative_inverse(e, phi)
    return (n, e, d)

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)




import random
import fractions
from prime_gen import generate_random_prime

def extended_gcd(a, b):
    #Returns pair (x, y) such that xa + yb = gcd(a, b)
    x = 0 
    lastx = 1 
    y = 1
    lasty = 0
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return lastx, lasty


def multiplicative_inverse(e, n):
    #Find the multiplicative inverse of e mod n.
    x, y = extended_gcd(e, n)
    if x < 0:
        return n + x
    return x

def rsaGenerateKeyManual(p,q):
	if p==q:
		print("Valores não válidos, devem ser diferentes.")
	elif p*q <= 256:
		print("Valores não válidos, p*q deve ser maior que 256.")
	else:
		n = p*q
		phi = (p-1)*(q-1)
		while True:
			e = random.randint(3, phi-1)
			if fractions.gcd(e,phi) == 1:
				break
		return (n,e)

def rsa_generate_key(bits):
    p = generate_random_prime(int(bits / 2))
    q = generate_random_prime(int(bits / 2))
    # Ensure q != p, though for large values of bits this is
    # statistically very unlikely
    while q == p and q*p < 256:
        q = generate_random_prime(int(bits / 2))
    n = p * q
    phi = (p - 1) * (q - 1)
    # Here we pick a random e, but a fixed value for e can also be used.
    while True:
        e = random.randint(3, phi - 1)
        if fractions.gcd(e, phi) == 1:
            break
    return (n, e, p, q)

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    key = int(key)
    n = int(n)
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m with fast modular exponentiation
    cipher = [str(pow(ord(char),key,n)) for char in plaintext]
    #Return the array of bytes
    return ' '.join(cipher)

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    ciphertext = ciphertext.split()
    p,q,e = pk
    n = p*q
    phi = (p-1)*(q-1)
    key = multiplicative_inverse(e,phi)
    #Generate the plaintext based on the ciphertext and key using a^b mod m with fast modular exponentiation
    plain = [chr(pow(int(char),key,n)) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)



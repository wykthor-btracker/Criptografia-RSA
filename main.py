from rsa import rsa_generate_key
from rsa import encrypt
from rsa import decrypt

if __name__ == '__main__':
	n, e, d = rsa_generate_key(8)
	chavePriv = e, n
	chavePub = d, n

	print("\nChave privada: \n-Expoente: ",e,"\n-Modulus: ",n,"\n")
	print("Chave Publica: \n-Expoente: ",d,"\n-Modulus: ",n,"\n")

	message = input("Enter the message: ")
	cipherr = encrypt(chavePriv, message)
	print("Encrypted message: ", cipherr)
	trueText = decrypt(chavePub, cipherr)
	print("Decrypted message: " , trueText)

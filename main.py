#imports
from rsa import rsa_generate_key
from rsa import encrypt
from rsa import decrypt
from decorators import logged
#imports#

#variables
#variables#

#classes
#classes#

#functions
#functions#

#main
@logged("%b %d %Y - %H:%M:%S")
def main():
	n, e, d = rsa_generate_key(2048)
	chavePriv = e, n
	chavePub = d, n

	#print("\nChave privada: \n-Expoente: ",e,"\n-Modulus: ",n,"\n")
	#print("Chave Publica: \n-Expoente: ",d,"\n-Modulus: ",n,"\n")

	message = "batata"
	cipherr = encrypt(chavePub, message)
	#print("Encrypted message: ", cipherr)
	trueText = decrypt(chavePriv, cipherr)
	print("Decrypted message: " , trueText)
	with open("chavepublica.txt","w") as pubKey:
		pubKey.write(str(chavePub))
#main#

if __name__ == "__main__":
	main()

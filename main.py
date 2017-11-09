#imports
from rsa import rsa_generate_key
from rsa import encrypt
from rsa import decrypt
from decorators import logged
#imports#

#variables
mainText = """O que deseja fazer?
1. Encriptar mensagem
2. Decriptar mensagem
3. Gerar par de chaves
4. Sair
"""
#variables#

#classes
#classes#

#functions
#functions#

#main
@logged("%b %d %Y - %H:%M:%S")
def main():
	#n, e, d = rsa_generate_key(2048)
	#chavePriv = e, n
	#chavePub = d, n
	op = 0
	while op != 4:
		op = int(input(mainText))
		if(op == 1):
			d = int(input("Insira o expoente público d. "))
			n = int(input("Insira o módulo n. "))
			inputName= input("Insira o nome do arquivo de entrada. ")
			output = input("Insira o nome do arquivo de saída. ")
			with open(inputName,'r') as entrada:
				texto = encrypt((d,n),entrada.read())
			with open(output,'w') as saida:
				saida.write(texto)
			#with open(output,'w') as saida:
			#	saida.write(texto)
	#cipherr = encrypt(chavePub, message)
	#trueText = decrypt(chavePriv, cipherr)
	
#main#

if __name__ == "__main__":
	main()

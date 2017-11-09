#imports
from os import system
from rsa import rsa_generate_key
from rsa import encrypt
from rsa import decrypt
from decorators import logged
#imports#

#variables
mainText = """O que deseja fazer?
1. Encriptar mensagem
2. Desencriptar mensagem
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
	#n, e, d = rsaGenerateKeyManual(17,21)
	#chavePriv = e, n
	#chavePub = d, n
	op = 0
	while op != 4:
		system("clear")
		op = int(input(mainText))
		
		if(op == 1):
			e = input("Insira o expoente E selecionado.")
			n = input("Insira o módulo N selecionado.")
			text = input("Insira o texto a ser criptografado. ")
			output = input("Insira o nome do arquivo de saída. ")
			texto = encrypt((e,n),text)
			with open(output,'w') as saida:
				saida.write(texto)
		elif(op == 2):
			p = int(input("Insira o valor para P. "))
			q = int(input("Insira o valor para Q. "))
			e = int(input("Insira o valor para E. "))
			inputName = input("Insira o nome do arquivo de entrada. ")
			with open(inputName,'r') as entrada:
				print(decrypt((p,q,e),entrada.read() ))
			input("aperte enter para continuar")
		elif(op == 3):
			choose = input("Deseja inserir os valores para a chave manualmente?(s/n). ")
			while(choose != 's' and choose != 'n'):
				choose = input("Entrada inválida, por favor declare se deseja inserir valores manualmente.(s/n). ")
			if(choose == 'n'):
				size = int(input("Insira o tamanho da chave em bytes. Ex: 512, 1024, 2048. "))
				n, e, p, q = rsa_generate_key(size)
				with open("chavepub.txt","w") as chavepub:
					chavepub.write("e = "+str(e)+" n = "+str(n)+" p = "+str(p)+" q = "+str(q))
				input("N = "+str(n)+"\n e = "+str(e)+"\n p = "+str(p)+"\n q = "+str(q))
	#cipherr = encrypt(chavePriv, message)
	#trueText = decrypt(chavePub, cipherr)
	
#main#

if __name__ == "__main__":
	main()

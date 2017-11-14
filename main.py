#imports
from os import system
from rsa import rsa_generate_key
from rsa import encrypt
from rsa import decrypt
from decorators import logged
#imports#

#variables
mainText = """
O que deseja fazer?
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
			try:
				e = int(input("Insira o expoente E selecionado."))
				n = int(input("Insira o módulo N selecionado."))
			except:
				input("Parâmetros inválidos insira inteiros positivos")
				continue
			text = input("Insira o texto a ser criptografado. ")
			output = input("Insira o nome do arquivo de saída. ")
			try:
				texto = encrypt((e,n),text)
				with open(output,'w') as saida:
					saida.write(texto)
			except:
				input("Parâmetros inválidos. Aperte enter para voltar.")
				continue
		elif(op == 2):
			try:
				p = int(input("Insira o valor para P. "))
				q = int(input("Insira o valor para Q. "))
				e = int(input("Insira o valor para E. "))
			except:
				print("Valores inválidos,")
				continue
			inputName = input("Insira o nome do arquivo de entrada. ")
			try:
				with open(inputName,'r') as entrada:
					print(decrypt((p,q,e),entrada.read() ))

				input("aperte enter para continuar")
			except:
				print("Parâmetros inválidos, aperte enter para voltar ao início.")
				continue
		elif(op == 3):
			try:
				size = int(input("Insira o número de bytes para ser usado no tamanho das chaves. Ex: 512, 1024, 2048. "))
			except:
				print("Favor insira um inteiro positivo.")
				continue
			n, e, p, q = rsa_generate_key(size)
			with open("chavepub.txt","w") as chavepub:
				chavepub.write("e = "+str(e)+" n = "+str(n)+" p = "+str(p)+" q = "+str(q))
			input("N = "+str(n)+"\n e = "+str(e)+"\n p = "+str(p)+"\n q = "+str(q)+"\n")
	#cipherr = encrypt(chavePriv, message)
	#trueText = decrypt(chavePub, cipherr)
	
#main#

if __name__ == "__main__":
	main()

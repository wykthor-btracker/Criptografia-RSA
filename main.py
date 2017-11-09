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
			d = input("Insira o expoente D selecionado. ")
			n = input("Insira o módulo N selecionado. ")
			inputName = input("Insira o nome do arquivo de entrada. ")
			with open(inputName,'r') as entrada:
				print(decrypt((d,n),entrada.read()))
			input("aperte enter para continuar")
		elif(op == 3):
			choose = input("Deseja inserir os valores para a chave manualmente?(s/n). ")
			while(choose != 's' and choose != 'n'):
				choose = input("Entrada inválida, por favor declare se deseja inserir valores manualmente.(s/n). ")
			if(choose == 'n'):
				size = int(input("Insira o tamanho da chave em bytes. Ex: 512, 1024, 2048. "))
				n, e, d = rsa_generate_key(size)
				with open("chavepub.txt","w") as chavepub:
					chavepub.write("d = "+str(d)+" n = "+str(n))
				with open("chavepriv.txt","w") as chavepriv:
					chavepriv.write("e = "+str(e)+" n = "+str(n))	
				print("N = "+str(n)+"\n e = "+str(e)+"\n d = "+str(d))
				input("Aperte enter para continuar.")
	#cipherr = encrypt(chavePriv, message)
	#trueText = decrypt(chavePub, cipherr)
	
#main#

if __name__ == "__main__":
	main()

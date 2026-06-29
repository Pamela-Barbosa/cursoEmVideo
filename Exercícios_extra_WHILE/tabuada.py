#Peça pro usuário digitar um número, imprima a tabuada desse número, conforme abaixo:

numero = int(input("Digite um número: "))
contador = 0

while contador < 10:
	contador += 1
	print(f"{numero} * {contador}")
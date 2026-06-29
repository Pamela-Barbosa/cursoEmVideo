#Imprima na tela o padrão de números abaixo 
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

numeros = []

contador = 0

while contador < 5:
	contador += 1
	numeros.append(contador)
	for num in numeros:
		print(num, end=" ")
	print()

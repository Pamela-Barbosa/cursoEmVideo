#Peça pro usuário digitar números, some cada número na variável "soma".
#  Quando ele digitar zero, encerre o programa e imprima a soma de todos números.

soma = 0
while True:
	numero = int(input("Digite um número: "))
	
	if numero == 0:
		break
	else:
		soma += numero
print(f"A soma dos números deu: {soma}")
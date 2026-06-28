soma = 0

for numero in range(1,3):
	numeros = int(input(f"Digite o {numero} número: ")) 
	if numeros % 2 == 0:
		soma += numeros

print(f"A soma dos número pares deu: {soma}")
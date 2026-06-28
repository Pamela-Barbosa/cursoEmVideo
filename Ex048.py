soma = 0

numInicial = int(input("Digite o número inicial: "))
razao =  int(input("Digite o número da razão que deseja: "))

for num in range(0, 10):
	if(num == 0):
		soma += numInicial 
	else:
		soma += razao
	print(soma)
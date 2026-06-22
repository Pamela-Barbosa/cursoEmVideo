import random

numeroSorte = int(input("\nDigite um número de 1 a 5: "))

numComputador = random.randint(1,5)

if numeroSorte == numComputador:
	print(f"Parabéns! Você acertou o número premiado: {numComputador}")
	print(f"Seu número: {numeroSorte}")
else:
	print(f"Ops.. O número {numeroSorte} informado não deu certo. Tente novamente!")
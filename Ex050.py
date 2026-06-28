frases = input("Digite uma frase: ")

frase_limpa = "".join(frases.split())

frase_invertida = ""

for frase in range(len(frase_limpa) -1,-1,-1):
	frase_invertida += frase_limpa[frase]

print(f"O inverso de {frase_limpa} é {frase_invertida}.")
if frase_invertida == frase_limpa:
	print("É uma frase palíndromo!")
else:
	print("Não é uma frase palíndromo!")

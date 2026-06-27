numeros = [9, 8, 2, 304, 55, 12, 95, 706, 215]
pares = []
impares = []

for numero in numeros:
	if numero % 2 == 0:
		pares.append(numero)
	else:
		impares.append(numero)

print(f"Os número Pares são: {pares}")
print(f"Os número Ímpares são: {impares}")
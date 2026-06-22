distanciaViagem = float(input("\nDigite a distância da sua viagem em km (10): "))

if distanciaViagem <= 200:
	precoViagem = distanciaViagem * 0.50
	print(f"O valor da sua passagem é: {precoViagem}")
else:
	precoViagem = distanciaViagem * 0.45
	print(f"O valor da sua passagem é: {precoViagem}")
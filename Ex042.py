peso = float(input("\nDigite seu peso: "))
altura = float(input("\nDigite sua altura: "))

calculoIMC = peso / altura**2

if calculoIMC < 18.5:
	print(f"Abaixo do peso, seu IMC é: {calculoIMC:.2f}!")
elif calculoIMC > 18.5 and calculoIMC < 25:
	print(f"Peso ideal, seu IMC é: {calculoIMC:.2f}!")
elif calculoIMC >= 25 and calculoIMC < 30:
	print(f"Sobrepeso, seu IMC é: {calculoIMC:.2f}!")
elif calculoIMC >=30 and calculoIMC < 40:
	print(f"Obesidade, seu IMC é: {calculoIMC:.2f}!")
else:
	print("Obesidade Mórbida, seu IMC é: {calculoIMC:.2f}!")

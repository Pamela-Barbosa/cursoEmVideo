num1 = int(input("\nDigite um número: "))
num2 = int(input("\nDigite o segundo número: "))

if num1 > num2:
	print(f"\nO número {num1} é maior que o número {num2}")
elif num2 > num1:
	print(f"\nO número {num2} é maior que o número {num1}")
else:
	print(f"\nOs números {num1} e {num2} são iguais")
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))
num3 = int(input("\nDigite o terceiro número: "))

if num1 > num2 and num1 > num3:
	print("\nO primeiro número é maior")
elif num2 > num1 and num2 > num3:
	print("\nO segundo número é maior")
else:
	print("\nO terceiro número é maior")
salario = float(input("\nDigite seu salário: "))

if salario > 1250:
	aumento = salario * 0.10
	salarioAjustado = salario + aumento
	print(f"\nParabéns! Você recebeu um aumento de 10%\nSeu novo salário é: {salarioAjustado}R$")
else:
	aumento = salario * 0.15
	salarioAjustado = salario + aumento
	print(f"\nParabéns! Você recebeu um aumento de 15%\nSeu novo salário é: {salarioAjustado}R$")
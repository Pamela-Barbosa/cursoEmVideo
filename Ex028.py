velocidadeCarro = int(input("\nDigite a velecidade do carro (80 km): "))

if velocidadeCarro > 80:
	calculoMulta = (velocidadeCarro - 80)
	calculoMultaValor = calculoMulta * 7
	print(f'Multado! O Valor da multa é: {calculoMultaValor}')
else:
	('Velocidade permitida.')
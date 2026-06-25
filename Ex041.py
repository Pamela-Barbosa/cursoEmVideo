lado1 = int(input("Digite um número para o primeiro lado do triangulo: "))
lado2 = int(input("Digite um número para o segundo lado do triangulo: "))
lado3 = int(input("Digite um número para o terceiro lado do triangulo: "))

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
	print("Triângulo Equilátero: Todos os lados iguais")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3 :
	print("Escaleno: Apenas dois lados iguais e um diferente")
else:
	print("Isósceles: apenas dois lados são diferentes")
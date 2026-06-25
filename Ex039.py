nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))


mediaNotas = (nota1 + nota2) /2

if mediaNotas < 5.0:
	print(f"Infelizmente você foi Reprovado, sua média é: {mediaNotas}")
elif mediaNotas > 5.0 and mediaNotas < 6.9:
	print(f"Você ficou de Recuperação, sua média é: {mediaNotas}")
else:
	print(f"Parabéns! você foi Aprovado, sua média é: {mediaNotas}")
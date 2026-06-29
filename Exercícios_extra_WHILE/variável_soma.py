#Peça para o usuário digitar números, cada número adicione na variável "soma". 
# Quando a variável soma atingir 50, encerre o programa

soma = 0

while True:
	numero = int(input("Digite um número: "))
	soma += numero
	if soma > 50:
		break
	else:
		print(soma)
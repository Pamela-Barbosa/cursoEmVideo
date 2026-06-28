from datetime import date

ano_atual = date.today().year

maiorIdade = []
menorIdade = []

for idade in range(1, 8):
	ano_nascimento = int(input("Digite o ano que você nasceu: "))
	calculoNascimento = ano_atual - ano_nascimento
	
	if calculoNascimento < 18:
		menorIdade.append(calculoNascimento)
	else:
		maiorIdade.append(calculoNascimento)

print(f"Pessoas que não atingiram a maior idade :", end="")
print(len(menorIdade))
print(f"Pessoas que atingiram a maior idade: ", end="")
print(len(maiorIdade))
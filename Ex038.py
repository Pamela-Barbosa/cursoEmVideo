ano_nascimento = int(input("Digite o ano que você nasceu (ex:1970): "))

calculoNascimento = 2026 - ano_nascimento
atrasoAlistamento = calculoNascimento - 18

if calculoNascimento < 18:
	tempoFaltaAlistamento = calculoNascimento - 18 

	print("\nVocê terá que se alistar ao serviço militar!")
	print(f"Falta {tempoFaltaAlistamento} anos para vc se alistar!")
elif calculoNascimento == 18:
	 print(f"\nVocê está dentro do período de alistamento, deve comparecer a junta militar!")
else:
	print(f"\nVocê passou do período de alistamento, deve comparecer a junta militar!")
	print(f"Você passou {atrasoAlistamento} anos do prazo do alistamento")

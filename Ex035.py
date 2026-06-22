valCasa = float(input("\nDigite o valor da casa que você deseja comprar: R$ "))
valSalario= float(input("Qual o valor da sua renda? R$ "))
anos = int(input("Quantos anos deseja pagar? "))

mesesPagando = anos * 12
prestMensal = valCasa / mesesPagando
limEmprestimo = valSalario * 0.30 

if prestMensal > limEmprestimo:
	print(f"\nEmprestimo indisponível! O valor da prestação mensal excedeu 30% do seu salário: {prestMensal:.2f}")
else:
	print(f"\nparabéns! Emprestimo Valido. o financiamento pode ser efetuado.")
	print(f'O valor da prestação é {prestMensal:.2f}, durante {mesesPagando} meses')
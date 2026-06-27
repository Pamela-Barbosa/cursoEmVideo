cadastros = [
	{'nome': 'Felipe', 'idade': 15},
	{'nome': 'Luana', 'idade': 25},
	{'nome': 'Kaio', 'idade': 18},
	{'nome': 'Maria', 'idade': 35},
	{'nome': 'cristiana', 'idade': 12},
]

maiorIdade = []
menorIdade = []

for cadastro in cadastros:
	if cadastro['idade'] < 18:
		menorIdade.append(cadastro['nome'])
	else:
		maiorIdade.append(cadastro['nome'])

print(f"Lista pessoas maiores de idade: {maiorIdade}")
print(f"Lista pessoas maiores de idade: {menorIdade}")
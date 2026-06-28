pesoColetados = []


for peso in range(1, 6):
	pesoPessoas = float(input("Digite seu peso atual (Ex: 78) kl: "))
	pesoColetados.append(pesoPessoas)

pesoColetados.sort()

print(f"O menor peso digitado foi: {pesoColetados[0]} kl")
print(f"O maior peso digitado foi: {pesoColetados[-1]} kl")
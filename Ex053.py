pessoas = []
"""tenho que terminar de fazer essa tarefa"""

for cadastro in range(1, 5):
	nome = input("Digite seu nome: ")
	idade = int(input("Digite sua idade: "))
	sexo = int(input("Qual seu gênero\n 1 - Femenino:\n 2 - Masculino:\nResposta: "))
	pessoas.append({"nome": nome ,"idade": idade, "sexo": sexo})


maiorHomem=0
nomeHomem=''
menorMulher=0
mediaHomem=0	
mediaMulher=0	
for pessoa in pessoas:
	
	if pessoa['sexo'] == 2:
		mediaHomem += pessoa['idade']
		if maiorHomem == 0:
			maiorHomem = pessoa['idade']
			nomeHomem = pessoa['nome']
		elif  pessoa['idade'] > maiorHomem:
			maiorHomem = pessoa['idade']
			nomeHomem = pessoa['nome']
	else:
		mediaMulher += pessoa['idade']
		if menorMulher == 0:
			menorMulher = pessoa['idade']
		elif  pessoa['idade'] < menorMulher:
			menorMulher = pessoa['idade']
			 	
print(maiorHomem)
print(mediaHomem/2)
print(mediaMulher/2)



# mediaIdade = (idade  2) / 4

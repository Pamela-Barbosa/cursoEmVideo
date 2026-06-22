import random

#random.choice() é utilizado para escolher de forma aleatória um nome
#random.sample( ,k=3(qntas pessoas sortea..)) utilizado para escolher mais de um sorteado sem repetir
#random.choices(, k=3(qnt pessoas...)) utilizado para escolher mais de um sorteado com repetição


lista_alunos = ["Paulo", "Pâmela", "Thiago", "Junior"]

sortAluno = random.choice(lista_alunos)
print(f"O Aluno escolhido é: {sortAluno}")

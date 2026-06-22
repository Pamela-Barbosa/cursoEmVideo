import random

apresen_alunos = ['Joana', 'Pedro', 'Bianca', 'Rafael']

sorteio = random.sample(apresen_alunos, k=4)
print(f"A ordem das apresentações é: {sorteio}")
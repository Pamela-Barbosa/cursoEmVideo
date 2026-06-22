nome = input("\nDigite seu nome completo: ")

print(f"\nSeu nome completo todo em letra de Forma: \n{nome.upper()}")
print(f"\nSeu nome completo todo em letra Minúscula: \n{nome.lower()}")
print(f"\nQuantidade de letra do seu nome completo: \n{len(nome.replace(" ",""))}")
print(f"\nQuantas letras tem o primeiro nome: \n{len(nome.split()[0])}") 
# len(nome.split()[0]) primeiro vai colocar o txt em um array usando o split() e pegar a posição 0 [0]
# e dois vai usar o len () para saber quantas letras tem o primeiro nome 


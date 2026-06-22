cidade = input('\nDigite o nome de uma cidade: ')
print(f"\nA cidade digitada começa com o nome 'santo'") #, end="" serve para juntar dois print
print("santo" in cidade.split()[0]) # aqui estou verificando se na frase cidade digitada começa com a palavra "santo"
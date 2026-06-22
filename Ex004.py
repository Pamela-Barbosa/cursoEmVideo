n = input("\nDigite algo: ")

print("\nQual o tipo da informação digitada? ",type(n))
print("A informação digitada é letra? ", n.isalpha())  #Verifica se o que foi digitado é Letra (True or False) 
print("A informação digitada é Número? ", n.isnumeric()) #Verifica se o que foi digitado é Numero (True or False) 
print("A informação digitada é Numero ou Letra? ",n.isalnum())  #Verifica se o que foi digitado é numero OR letra (True or False) 
print("A informação digitada é toda em Maiúsculo ",n.isupper())  #Verifica se o que foi digitado é letras em Maiusculo (True or False) 
print("A informação digitada é toda em Minúsculo?", n.islower()) #Verifica se o que foi digitado é letras em Minúsculo (True or False) 
print("-" * 20)

	
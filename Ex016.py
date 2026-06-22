import math

# math.floor() serve para arredondar para baixo
# math.trunc(x): Corta a parte fracionária. Ele joga fora tudo o que está depois do ponto
numero = float(input("Digite um numero float: "))
print(f"O número {numero}, tem parte inteira {math.trunc(numero)}")
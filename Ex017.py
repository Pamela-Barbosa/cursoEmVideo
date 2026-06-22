import math

cat_oposto = int(input("\nDigite o número do Cateto Oposto: ")) 
cat_adjacente = int(input("Digite o número do Cateto Adjacente: ")) 

Cal_Hipotenusa = math.hypot(cat_oposto, cat_adjacente)

print(f"\nO comprimento da Hipotenusa é: {Cal_Hipotenusa}")
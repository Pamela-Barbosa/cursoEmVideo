reta1 = int(input("\nDigite o tamanho da reta 1 (ex: 5): "))
reta2 = int(input("\nDigite o tamanho da reta 2 (ex: 5): "))
reta3 = int(input("\nDigite o tamanho da reta 3 (ex: 5): "))

max = 0
soma= 0
if reta1 > reta2 and reta1 > reta3 :
	max = reta1
	soma = reta2 + reta3
elif reta2 > reta3 and reta2 > reta1:
	max = reta2
	soma = reta1 + reta3
else:
	max = reta3
	soma = reta1 + reta2

if soma > max :
	print("Não Formam um triângulo")
else:
	print("Forma um triangulo")
numeros = [9, 8, 2, 304, 55, 12, 95, 706, 215, 908, 201, 4]

for numero in numeros:
	if numero > 200:
		break  #Com o break ele fecha a lista no momento que ele encontra o 304
				#, e não ler os números depois que entraria na condiação, como o 55,12,95...
	print(numero)
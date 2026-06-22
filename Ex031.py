ano = int(input("\nDigite um ano (ex:2021): "))

if ano % 4 == 0 and ano % 100 !=0 and ano % 400 == 0:
	print(f"\nÉ um ano bissexto: {ano}")
else:
	print(f"\nNão é um ano bissexto: {ano}")
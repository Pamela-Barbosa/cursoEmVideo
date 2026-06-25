anoNascimento = int(input("\nDigite o ano do seu nascimento: "))

calculoNascimento = 2026 - anoNascimento

if calculoNascimento <= 9:
	print("Categoria: Mirim")
elif calculoNascimento <=14:
	print("Categoria: Infantil")
elif calculoNascimento <=19:
	print("Categoria: Junior")
elif calculoNascimento <=20:
	print("Categoria: Senior")
else:
	print("Categoria: Master")
